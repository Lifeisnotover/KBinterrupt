import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.health = 10
        self.projectiles = []
        self.shoot_cooldown = 0
        self.image = pygame.image.load('../character.png')
        self.image = pygame.transform.scale(self.image, (PLAYER_SIZE, PLAYER_SIZE))

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        for proj in self.projectiles:
            color = WHITE if proj['type'] == '1' else PURPLE
            pygame.draw.circle(surface, color, (int(proj['x']), int(proj['y'])), PROJECTILE_SIZE)

    def move(self, dx, dy, rooms):
        self.rect.x += dx
        self.rect.y += dy
        for room in rooms:
            if not room.rect.contains(self.rect):
                self.rect.x -= dx
                self.rect.y -= dy
                break

    def shoot(self, current_room):
        if self.shoot_cooldown <= 0 and current_room.mobs:
            closest_mob = min(
                current_room.mobs,
                key=lambda mob: ((self.rect.centerx - mob['x']) ** 2 + (self.rect.centery - mob['y']) ** 2) ** 0.5
            )

            dx = closest_mob['x'] - self.rect.centerx
            dy = closest_mob['y'] - self.rect.centery
            length = (dx ** 2 + dy ** 2) ** 0.5
            if length > 0:
                dx, dy = dx / length, dy / length

            self.projectiles.append({
                'x': self.rect.centerx,
                'y': self.rect.centery,
                'dx': dx * 7,
                'dy': dy * 7,
                'type': random.choice(['0', '1'])
            })
            self.shoot_cooldown = 15

    def update_projectiles(self, current_room):
        for proj in self.projectiles[:]:
            proj['x'] += proj['dx']
            proj['y'] += proj['dy']

            for mob in current_room.mobs[:]:
                if ((proj['x'] - mob['x']) ** 2 + (proj['y'] - mob['y']) ** 2) ** 0.5 < MOB_SIZE + PROJECTILE_SIZE:
                    mob['health'] -= 1
                    if mob['health'] <= 0:
                        current_room.mobs.remove(mob)
                    if proj in self.projectiles:
                        self.projectiles.remove(proj)
                    break

            if not current_room.rect.collidepoint(proj['x'], proj['y']):
                if proj in self.projectiles:
                    self.projectiles.remove(proj)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1