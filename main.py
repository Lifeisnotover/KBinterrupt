import pygame
import sys
from settings import *
from room import create_dungeon
from entities.player import Player
from entities.mob import Mob
from game import show_game_over, draw_game_info

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Рогалик с боями")
    clock = pygame.time.Clock()

    images = load_images()
    if images is None:
        return

    rooms = create_dungeon(images)
    player = Player(WIDTH // 2, HEIGHT // 2, images)
    current_room = rooms[0]
    mob_system = Mob()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_e:
                    for door in current_room.doors:
                        if player.rect.colliderect(door['rect']):
                            current_room = door['target']
                            if door['direction'] == 'north':
                                player.rect.bottom = current_room.rect.bottom - 10
                            elif door['direction'] == 'south':
                                player.rect.top = current_room.rect.top + 10
                            elif door['direction'] == 'west':
                                player.rect.right = current_room.rect.right - 10
                            elif door['direction'] == 'east':
                                player.rect.left = current_room.rect.left + 10
                            break

        if player.health <= 0:
            if show_game_over(screen):
                rooms = create_dungeon(images)
                player = Player(WIDTH // 2, HEIGHT // 2, images)
                current_room = rooms[0]
            continue

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