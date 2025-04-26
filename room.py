import pygame
import random
from settings import *


class Room:
    def __init__(self, x, y, w, h, name):
        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.color = (100, 100, 255)
        self.doors = []
        self.mobs = []
        self.background = pygame.image.load('images/room_background.png')
        self.background = pygame.transform.scale(self.background, (200, 200))

    def draw(self, surface, player_rect=None):
        surface.blit(self.background, self.rect.topleft)
        pygame.draw.rect(surface, self.color, self.rect, 2)

        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, WHITE)
        surface.blit(text, (self.rect.x + 10, self.rect.y + 10))

        for door in self.doors:
            color = YELLOW if player_rect and player_rect.colliderect(door['rect']) else GREEN
            pygame.draw.rect(surface, color, door['rect'], 2)

        for mob in self.mobs:
            pygame.draw.circle(surface, BLUE, (mob['x'], mob['y']), MOB_SIZE)

    def add_door(self, direction, target_room):
        if direction == 'north':
            rect = pygame.Rect(self.rect.centerx - DOOR_SIZE // 2, self.rect.top - DOOR_SIZE // 2, DOOR_SIZE, DOOR_SIZE)
        elif direction == 'south':
            rect = pygame.Rect(self.rect.centerx - DOOR_SIZE // 2, self.rect.bottom - DOOR_SIZE // 2, DOOR_SIZE,
                               DOOR_SIZE)
        elif direction == 'west':
            rect = pygame.Rect(self.rect.left - DOOR_SIZE // 2, self.rect.centery - DOOR_SIZE // 2, DOOR_SIZE,
                               DOOR_SIZE)
        elif direction == 'east':
            rect = pygame.Rect(self.rect.right - DOOR_SIZE // 2, self.rect.centery - DOOR_SIZE // 2, DOOR_SIZE,
                               DOOR_SIZE)

        self.doors.append({'rect': rect, 'direction': direction, 'target': target_room})

    def spawn_mobs(self, count):
        for _ in range(count):
            x = random.randint(self.rect.left + MOB_SIZE, self.rect.right - MOB_SIZE)
            y = random.randint(self.rect.top + MOB_SIZE, self.rect.bottom - MOB_SIZE)
            self.mobs.append({'x': x, 'y': y, 'health': 2})


def create_dungeon():
    rooms = []
    room1 = Room(300, 200, 200, 200, "Главный зал")
    room2 = Room(100, 200, 200, 200, "Кладовая")
    room3 = Room(300, 0, 200, 200, "Арсенал")
    room4 = Room(500, 200, 200, 200, "Библиотека")
    room5 = Room(300, 400, 200, 200, "Тайная комната")

    room1.add_door('west', room2)
    room1.add_door('north', room3)
    room1.add_door('east', room4)
    room1.add_door('south', room5)

    room2.add_door('east', room1)
    room3.add_door('south', room1)
    room4.add_door('west', room1)
    room5.add_door('north', room1)

    for room in [room1, room2, room3, room4, room5]:
        room.spawn_mobs(3)

    return rooms