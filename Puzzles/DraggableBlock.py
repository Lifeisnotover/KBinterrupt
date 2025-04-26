import pygame
from KBinterrupt.settings import *
class DraggableBlock:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 100, 50)
        self.text = text
        self.dragging = False
        self.font = pygame.font.SysFont(None, FONT_SIZE)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.rect.move_ip(event.rel)

    def update(self):
        pass

    def myDraw(self, screen):
        pygame.draw.rect(screen, LIGHT_BLUE, self.rect)
        text_surf = self.font.render(self.text, True, BLACK)
        screen.blit(text_surf, (self.rect.x + 5, self.rect.y + 10))
