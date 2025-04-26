import pygame
from settings import *

class ChoiceButton:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 150, 50)
        self.text = text
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.selected = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.selected = not self.selected

    def myDraw(self, screen):
        color = GREEN if self.selected else RED
        pygame.draw.rect(screen, color, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))
