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

    return True


def draw_game_info(screen, current_room, player, images):
    font = pygame.font.SysFont(None, 30)

    # Отображение названия комнаты
    room_text = font.render(f"Комната: {current_room.name}", True, WHITE)
    screen.blit(room_text, (TEXT_OFFSET, TEXT_OFFSET))

    # Позиция для первого сердца
    heart_x = TEXT_OFFSET
    heart_y = TEXT_OFFSET + room_text.get_height() + 10

    # Получаем изображения сердец из словаря
    heart_img = images['heart'][0]  # Полное сердце (первый элемент списка)
    empty_heart_img = images['empty_heart'][0]  # Пустое сердце

    # Отображаем сердца - сначала полные, затем пустые
    for i in range(player.max_health):
        if i < player.health:
            screen.blit(heart_img, (heart_x + i * (HEART_SIZE + HEART_SPACING), heart_y))
        else:
            screen.blit(empty_heart_img, (heart_x + i * (HEART_SIZE + HEART_SPACING), heart_y))