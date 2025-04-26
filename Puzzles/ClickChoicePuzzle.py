import pygame
from settings import *


class ClickChoicePuzzle:
    def __init__(self, screen, question, answers, correct_answer):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', FONT_SIZE)
        self.buttons = []
        self.completed = False
        self.task_text = question
        self.answers = answers
        self.correct_answer = correct_answer

        max_text_width = max([self.font.size(answer)[0] for answer in self.answers])

        button_width = max(max_text_width + 40, 120)
        button_height = 50
        button_margin = 20

        max_buttons_per_row = (WIDTH - 2 * button_margin) // (button_width + button_margin)

        start_y = HEIGHT // 2 + 50

        for i, answer in enumerate(self.answers):
            row = i // max_buttons_per_row
            pos_in_row = i % max_buttons_per_row

            total_buttons_in_row = min(len(self.answers) - row * max_buttons_per_row, max_buttons_per_row)
            row_width = total_buttons_in_row * button_width + (total_buttons_in_row - 1) * button_margin
            start_x = (WIDTH - row_width) // 2

            x = start_x + pos_in_row * (button_width + button_margin)
            y = start_y + row * (button_height + button_margin)

            self.buttons.append({
                'rect': pygame.Rect(x, y, button_width, button_height),
                'text': answer,
                'color': LIGHT_BLUE,
                'original_text': answer
            })

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            for button in self.buttons:
                if button['rect'].collidepoint(pos):
                    if button['original_text'] == self.correct_answer:
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
            pygame.draw.rect(self.screen, button['color'], button['rect'], border_radius=10)

            text = button['original_text']
            text_surf = self.font.render(text, True, BLACK)

            if text_surf.get_width() > button['rect'].width - 20:
                while text_surf.get_width() > button['rect'].width - 20 and len(text) > 3:
                    text = text[:-1]
                    text_surf = self.font.render(text + "...", True, BLACK)

            text_rect = text_surf.get_rect(center=button['rect'].center)
            self.screen.blit(text_surf, text_rect)

    def is_completed(self):
        return self.completed