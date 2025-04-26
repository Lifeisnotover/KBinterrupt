import pygame
import sys
from settings import *


def show_game_over(screen):
    font = pygame.font.SysFont(None, 72)
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))

    font = pygame.font.SysFont(None, 36)
    text = font.render("Нажми R чтобы перезапустить", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    return True  # Indicates game should restart


def draw_game_info(screen, current_room, player):
    font = pygame.font.SysFont(None, 30)
    info = [
        f"Комната: {current_room.name}",
        f"Здоровье: {'♥' * int(player.health)}",
    ]
    for i, text in enumerate(info):
        text_surface = font.render(text, True, WHITE)
        screen.blit(text_surface, (10, 10 + i * 30))