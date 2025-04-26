import pygame
import sys
from settings import *

def show_main_menu(screen):
    background_image = pygame.image.load('Images/menu_background.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    font_title = pygame.font.Font('Fonts/alagard-12px-unicode.otf', 48)
    font_option = pygame.font.Font('Fonts/alagard-12px-unicode.otf', 32)

    title_text = font_title.render("KBInterrupt", True, WHITE)
    start_text = font_option.render("Начать игру", True, WHITE)
    quit_text = font_option.render("Выйти", True, WHITE)

    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    button_width = 300
    button_height = 60
    start_button_rect = pygame.Rect(0, 0, button_width, button_height)
    start_button_rect.center = start_rect.center
    quit_button_rect = pygame.Rect(0, 0, button_width, button_height)
    quit_button_rect.center = quit_rect.center

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

        alpha += alpha_direction * 5
        if alpha > 255:
            alpha = 255
            alpha_direction = -1
        elif alpha < 0:
            alpha = 0
            alpha_direction = 1

        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, (0, 0, 0, 128), start_button_rect)
        pygame.draw.rect(screen, (0, 0, 0, 128), quit_button_rect)

        title_text.set_alpha(alpha)
        start_text.set_alpha(alpha)
        quit_text.set_alpha(alpha)

        screen.blit(title_text, title_rect)
        screen.blit(start_text, start_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        pygame.time.delay(30)
