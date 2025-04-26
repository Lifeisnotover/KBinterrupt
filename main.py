import random
import sys

import pygame

from Puzzles.ClickChoicePuzzle import ClickChoicePuzzle
from entities.mob import Mob
from entities.player import Player
from game import show_game_over, draw_game_info
from room import create_dungeon
from settings import load_images, WIDTH, HEIGHT, BLACK

available_puzzles = [
    lambda screen: ClickChoicePuzzle(
        screen,
        "Что выведет этот код?\n\nint main() {\n  int x = 5;\n  int y = x++ + ++x;\n  cout << y;\n  return 0;\n}",
        ["10", "11", "12", "13"],
        "12"
    ),
    lambda screen: ClickChoicePuzzle(
        screen,
        "Какая сложность у быстрой сортировки\nв среднем случае?",
        ["O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
        "O(n log n)"
    ),
    lambda screen: ClickChoicePuzzle(
        screen,
        "Какой алгоритм использует Dijkstra\nдля нахождения кратчайшего пути?",
        ["Жадный", "Разделяй и властвуй", "Динамическое программирование", "Полный перебор"],
        "Жадный"
    ),
    lambda screen: ClickChoicePuzzle(
        screen,
        "Что делает оператор '>>>' в Java?",
        ["Логическое И", "Беззнаковый сдвиг вправо", "Знаковый сдвиг вправо", "Логическое ИЛИ"],
        "Беззнаковый сдвиг вправо"
    ),
]


def adjust_player_position(player, door):
    """Корректирует позицию игрока при переходе через дверь"""
    if door['direction'] == 'north':
        player.rect.bottom = door['target'].rect.bottom - 10
    elif door['direction'] == 'south':
        player.rect.top = door['target'].rect.top + 10
    elif door['direction'] == 'west':
        player.rect.right = door['target'].rect.right - 10
    elif door['direction'] == 'east':
        player.rect.left = door['target'].rect.left + 10




def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Рогалик с головоломками")
    clock = pygame.time.Clock()

    images = load_images()
    if images is None:
        print("Не удалось загрузить изображения!")
        return

    rooms = create_dungeon(images)
    player = Player(WIDTH // 2, HEIGHT // 2, images)
    current_room = rooms[0]  # Главный зал
    mob_system = Mob()
    current_puzzle = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_e and current_puzzle is None:
                    for door in current_room.doors:
                        if player.rect.colliderect(door['rect']):
                            if door['target'].name == "Главный зал" or getattr(door['target'], "puzzle_solved", False):
                                current_room = door['target']
                                adjust_player_position(player, door)
                                break

                            if len(current_room.mobs) > 0:
                                break

                            if available_puzzles:
                                selected_creator = random.choice(available_puzzles)
                                current_puzzle = selected_creator(screen)
                                available_puzzles.remove(selected_creator)

                            break

            if current_puzzle:
                current_puzzle.handle_event(event)

        if player.health <= 0:
            if show_game_over(screen):
                rooms = create_dungeon(images)
                player = Player(WIDTH // 2, HEIGHT // 2, images)
                current_room = rooms[0]
            continue

        if current_puzzle:
            current_puzzle.update()
            current_puzzle.draw()

            if current_puzzle.is_completed():
                # Находим дверь, через которую пытались войти
                for door in current_room.doors:
                    if player.rect.colliderect(door['rect']):
                        door['target'].puzzle_solved = True
                        current_room = door['target']
                        adjust_player_position(player, door)
                        break
                current_puzzle = None
        else:
            player.update(current_room)

            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            if keys[pygame.K_w]: dy = -player.speed
            if keys[pygame.K_s]: dy = player.speed
            if keys[pygame.K_a]: dx = -player.speed
            if keys[pygame.K_d]: dx = player.speed
            player.move(dx, dy, [current_room])

            if keys[pygame.K_SPACE]:
                player.shoot(current_room)

            player.update_projectiles(current_room)
            mob_system.update_mobs(current_room, player)

            screen.fill(BLACK)
            current_room.draw(screen, player.rect)
            player.draw(screen)
            draw_game_info(screen, current_room, player)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
