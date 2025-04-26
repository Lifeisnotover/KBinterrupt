import pygame
import random
from settings import *


class Room:
    def __init__(self, x, y, w, h, name, images):
        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.color = (100, 100, 255)
        self.doors = []
        self.mobs = []
        self.images = images
        self.safe_period = 0  # Таймер защиты при входе (в кадрах)
        self.has_player = False  # Добавляем отсутствующий атрибут
        self.player_entered = False  # Факт входа игрока в комнату
        self.puzzle_solved = False

    def draw(self, surface, player_rect=None):
        # Проверяем, находится ли игрок в комнате
        current_has_player = player_rect and self.rect.colliderect(player_rect)

        # Если игрок только что вошел - запускаем таймер защиты
        if current_has_player and not self.has_player:
            self.safe_period = 60  # 1 секунда при 60 FPS
            self.player_entered = True

        self.has_player = current_has_player  # Обновляем статус

        # Отрисовка комнаты
        wall_rect = pygame.Rect(self.rect.x - 20, self.rect.y - 20, self.rect.w + 40, self.rect.h + 40)
        surface.blit(self.images['wall'], wall_rect.topleft)
        surface.blit(self.images['room_bg'], self.rect.topleft)

        # Отрисовка названия комнаты
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, WHITE)
        surface.blit(text, (self.rect.x + 10, self.rect.y + 10))

        # Отрисовка дверей
        for door in self.doors:
            color = YELLOW if player_rect and player_rect.colliderect(door['rect']) else GREEN
            pygame.draw.rect(surface, color, door['rect'], 2)

        # Отрисовка мобов
        for mob in self.mobs:
            # Пока действует защитный период, рисуем мобов полупрозрачными
            if self.safe_period > 0:
                mob_surface = self.images['mob'].copy()
                mob_surface.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)
                surface.blit(mob_surface, (mob['x'] - MOB_SIZE // 2, mob['y'] - MOB_SIZE // 2))
            else:
                surface.blit(self.images['mob'], (mob['x'] - MOB_SIZE // 2, mob['y'] - MOB_SIZE // 2))

    def update(self):
        # Уменьшаем таймер защиты
        if self.safe_period > 0:
            self.safe_period -= 1
        else:
            self.player_entered = False

    def can_attack(self):
        # Мобы могут атаковать только когда нет защитного периода и игрок в комнате
        return self.safe_period <= 0 and self.has_player

    def add_door(self, direction, target_room):
        if direction == 'north':
            rect = pygame.Rect(self.rect.centerx - DOOR_SIZE // 2, self.rect.top - DOOR_SIZE // 2, DOOR_SIZE, DOOR_SIZE)
        elif direction == 'south':
            rect = pygame.Rect(self.rect.centerx - DOOR_SIZE // 2, self.rect.bottom - DOOR_SIZE // 2, DOOR_SIZE, DOOR_SIZE)
        elif direction == 'west':
            rect = pygame.Rect(self.rect.left - DOOR_SIZE // 2, self.rect.centery - DOOR_SIZE // 2, DOOR_SIZE, DOOR_SIZE)
        elif direction == 'east':
            rect = pygame.Rect(self.rect.right - DOOR_SIZE // 2, self.rect.centery - DOOR_SIZE // 2, DOOR_SIZE, DOOR_SIZE)

        self.doors.append({'rect': rect, 'direction': direction, 'target': target_room})

    def spawn_mobs(self, count):
        for _ in range(count):
            side = random.choice(['top', 'bottom'])
            if side == 'top':
                x = random.randint(self.rect.left + MOB_SIZE, self.rect.right - MOB_SIZE)
                y = self.rect.top + MOB_SIZE
            elif side == 'bottom':
                x = random.randint(self.rect.left + MOB_SIZE, self.rect.right - MOB_SIZE)
                y = self.rect.bottom - MOB_SIZE
            self.mobs.append({'x': x, 'y': y, 'health': 2})

def create_dungeon(images):
    room1 = Room(300, 200, 200, 200, "Главный зал", images)
    room2 = Room(100, 200, 200, 200, "Кладовая", images)
    room3 = Room(300, 0, 200, 200, "Арсенал", images)
    room4 = Room(500, 200, 200, 200, "Библиотека", images)
    room5 = Room(300, 400, 200, 200, "Тайная комната", images)

    rooms = [room1, room2, room3, room4, room5]

    room1.add_door('west', room2)
    room1.add_door('north', room3)
    room1.add_door('east', room4)
    room1.add_door('south', room5)

    room2.add_door('east', room1)
    room3.add_door('south', room1)
    room4.add_door('west', room1)
    room5.add_door('north', room1)

    for room in rooms:
        room.spawn_mobs(3)

    return rooms
