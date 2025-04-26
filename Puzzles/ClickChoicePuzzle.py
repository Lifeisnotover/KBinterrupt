import pygame
from KBinterrupt.settings import *

class ClickChoicePuzzle:
    def __init__(self, screen, question, answers, correct_answer):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', FONT_SIZE)
        self.buttons = []
        self.completed = False
        self.task_text = question
        self.answers = answers
        self.correct_answer = correct_answer

        button_width = 200
        button_height = 50
        start_x = (WIDTH - (len(self.answers) * button_width)) // 2
        for i, answer in enumerate(self.answers):
            x = start_x + i * (button_width + 20)
            y = HEIGHT // 2 + 100
            self.buttons.append({
                'rect': pygame.Rect(x, y, button_width, button_height),
                'text': answer,
                'color': LIGHT_BLUE
            })

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for button in self.buttons:
                if button['rect'].collidepoint(pos):
                    if button['text'] == self.correct_answer:
                        button['color'] = GREEN
                        self.completed = True
                    else:
                        button['color'] = RED

    def update(self):
        pass

    def draw(self):
        self.screen.fill(WHITE)

        lines = self.task_text.split('\n')
        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, BLACK)
            self.screen.blit(text_surf, (WIDTH // 2 - text_surf.get_width() // 2, 100 + i * 30))

        for button in self.buttons:
            pygame.draw.rect(self.screen, button['color'], button['rect'])
            text_surf = self.font.render(button['text'], True, BLACK)
            text_rect = text_surf.get_rect(center=button['rect'].center)
            self.screen.blit(text_surf, text_rect)

    def is_completed(self):
        return self.completed