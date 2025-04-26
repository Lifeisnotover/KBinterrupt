import pygame
import sys
from settings import *

def show_main_menu(screen):
    # Загрузка фонового изображения
    background_image = pygame.image.load('Images/menu_background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    # Загрузка шрифтов
    font_title = pygame.font.Font('Fonts/alagard-12px-unicode.otf', 48)
    font_option = pygame.font.Font('Fonts/alagard-12px-unicode.otf', 32)

    # Создание текста
    title_text = font_title.render("KBInterrupt", True, WHITE)
    start_text = font_option.render("Начать игру", True, WHITE)
    quit_text = font_option.render("Выйти", True, WHITE)

    # Позиционирование текста
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    # Полупрозрачные плашки для кнопок
    button_width = 300
    button_height = 60
    start_button_rect = pygame.Rect(0, 0, button_width, button_height)
    start_button_rect.center = start_rect.center
    quit_button_rect = pygame.Rect(0, 0, button_width, button_height)
    quit_button_rect.center = quit_rect.center

    # Анимация мерцания текста
    alpha = 0
    alpha_direction = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return True
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        # Обновление анимации мерцания
        alpha += alpha_direction * 5
        if alpha > 255:
            alpha = 255
            alpha_direction = -1
        elif alpha < 0:
            alpha = 0
            alpha_direction = 1

        # Отрисовка фона
        screen.blit(background_image, (0, 0))

        # Отрисовка полупрозрачных плашек
        pygame.draw.rect(screen, (0, 0, 0, 128), start_button_rect)
        pygame.draw.rect(screen, (0, 0, 0, 128), quit_button_rect)

        # Отрисовка текста с мерцанием
        title_text.set_alpha(alpha)
        start_text.set_alpha(alpha)
        quit_text.set_alpha(alpha)

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        pygame.time.delay(30)
