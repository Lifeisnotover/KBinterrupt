import pygame
from source import puzzle_settings

class ChoiceButton:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 150, 50)
        self.text = text
        self.font = pygame.font.SysFont(None, puzzle_settings.FONT_SIZE)
        self.selected = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = not self.selected

    def myDraw(self, screen):
        color = puzzle_settings.GREEN if self.selected else puzzle_settings.RED
        pygame.draw.rect(screen, color, self.rect)
        text_surf = self.font.render(self.text, True, puzzle_settings.BLACK)
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))
