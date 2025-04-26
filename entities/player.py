
import random
from KBinterrupt.settings import *

class Player:
    def __init__(self, x, y, images):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.health = 10
        self.projectiles = []
        self.shoot_cooldown = 0
        self.images = images
        self.current_image = images['down'][0]
        self.animation_frame = 0
        self.animation_delay = 10
        self.animation_counter = 0
        self.last_direction = None
    def draw(self, surface):
        surface.blit(self.current_image, self.rect.topleft)
        for proj in self.projectiles:
            image = self.images['projectiles'][proj['type']]
            surface.blit(image, (int(proj['x'] - PROJECTILE_SIZE // 2), int(proj['y'] - PROJECTILE_SIZE // 2)))

    def move(self, dx, dy, rooms):
        self.rect.x += dx
        self.rect.y += dy
        for room in rooms:
            if not room.rect.contains(self.rect):
                self.rect.x -= dx
                self.rect.y -= dy
                break

        if dx > 0:
            self.update_animation('right')
        elif dx < 0:
            self.update_animation('left')
        elif dy > 0:
            self.update_animation('down')
        elif dy < 0:
            self.update_animation('up')

    def update_animation(self, direction):
        if direction != self.last_direction:
            self.animation_frame = 0
            self.last_direction = direction

        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0

            if direction in ['up', 'left', 'right', 'down'] and isinstance(self.images[direction], list):
                self.animation_frame = (self.animation_frame + 1) % len(self.images[direction])
                self.current_image = self.images[direction][self.animation_frame]

    def shoot(self, current_room):
        if self.shoot_cooldown <= 0 and current_room.mobs:
            closest_mob = min(
                current_room.mobs,
                key=lambda mob: ((self.rect.centerx - mob['x'])**2 + (self.rect.centery - mob['y'])**2)**0.5
            )

            dx = closest_mob['x'] - self.rect.centerx
            dy = closest_mob['y'] - self.rect.centery
            length = (dx**2 + dy**2)**0.5
            if length > 0:
                dx, dy = dx/length, dy/length

            projectile_type = random.choice(['0', '1'])
            self.projectiles.append({
                'x': self.rect.centerx,
                'y': self.rect.centery,
                'dx': dx * 7,
                'dy': dy * 7,
                'type': projectile_type
            })
            self.shoot_cooldown = 15

    def update_projectiles(self, current_room):
        for proj in self.projectiles[:]:
            proj['x'] += proj['dx']
            proj['y'] += proj['dy']

            for mob in current_room.mobs[:]:
                if ((proj['x'] - mob['x'])**2 + (proj['y'] - mob['y'])**2)**0.5 < MOB_SIZE + PROJECTILE_SIZE:
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