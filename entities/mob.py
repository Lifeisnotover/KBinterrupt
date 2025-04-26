import pygame
import random
from settings import *


class Mob:
    def update_mobs(self, current_room, player):
        for mob in current_room.mobs:
            if 'delay' not in mob:
                mob['delay'] = random.randint(30, 60)
            if mob['delay'] > 0:
                mob['delay'] -= 1
                continue

            dx = player.rect.centerx - mob['x']
            dy = player.rect.centery - mob['y']
            length = (dx ** 2 + dy ** 2) ** 0.5
            if length > 0:
                mob['x'] += dx / length * MOB_SPEED
                mob['y'] += dy / length * MOB_SPEED

            mob_rect = pygame.Rect(mob['x'] - MOB_SIZE // 2, mob['y'] - MOB_SIZE // 2, MOB_SIZE, MOB_SIZE)
            if mob_rect.colliderect(player.rect):
                player.take_damage(MOB_DAMAGE)