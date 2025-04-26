import random
from KBinterrupt.settings import *


class Player:
    def __init__(self, x, y, images):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.health = 10
        self.max_health = 10
        self.projectiles = []
        self.shoot_cooldown = 0
        self.shoot_delay = 45
        self.images = images
        self.current_image = images['down'][0]

        self.is_invincible = False
        self.invincibility_timer = 0
        self.invincibility_duration = 60
        self.blink_timer = 0
        self.blink_speed = 5
        self.visible = True
        self.hit_flash_timer = 0

    def move(self, dx, dy, rooms):
        old_pos = self.rect.copy()
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        for room in rooms:
            if not room.rect.contains(self.rect):
                self.rect = old_pos
                break

    def shoot(self, current_room=None):
        if self.shoot_cooldown <= 0:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 1

            if keys[pygame.K_LEFT]:
                dx, dy = -1, 0
            elif keys[pygame.K_RIGHT]:
                dx, dy = 1, 0
            elif keys[pygame.K_UP]:
                dx, dy = 0, -1
            elif keys[pygame.K_DOWN]:
                dx, dy = 0, 1

            self.projectiles.append({
                'x': self.rect.centerx,
                'y': self.rect.centery,
                'dx': dx * PROJECTILE_SPEED,
                'dy': dy * PROJECTILE_SPEED,
                'type': random.choice(['0', '1'])
            })
            self.shoot_cooldown = self.shoot_delay
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def take_damage(self, amount):
        if not self.is_invincible:
            self.health = max(0, self.health - amount)
            self.activate_invincibility()

    def activate_invincibility(self):
        """Активирует период неуязвимости"""
        self.is_invincible = True
        self.invincibility_timer = self.invincibility_duration
        self.hit_flash_timer = self.invincibility_duration

    def update(self, current_room):
        if self.is_invincible:
            self.invincibility_timer -= 1
            self.hit_flash_timer -= 1
            if self.invincibility_timer <= 0:
                self.is_invincible = False

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        self.update_projectiles(current_room)

    def update_projectiles(self, current_room):
        for proj in self.projectiles[:]:

            proj['x'] += proj['dx']
            proj['y'] += proj['dy']

            for mob in current_room.mobs[:]:
                mob_rect = pygame.Rect(mob['x'] - MOB_SIZE // 2, mob['y'] - MOB_SIZE // 2, MOB_SIZE, MOB_SIZE)
                proj_rect = pygame.Rect(proj['x'] - PROJECTILE_SIZE, proj['y'] - PROJECTILE_SIZE,
                                        PROJECTILE_SIZE * 2, PROJECTILE_SIZE * 2)

                if mob_rect.colliderect(proj_rect):
                    mob['health'] -= 1
                    if mob['health'] <= 0:
                        current_room.mobs.remove(mob)
                    self.projectiles.remove(proj)
                    break

            if not current_room.rect.collidepoint(proj['x'], proj['y']):
                self.projectiles.remove(proj)

    def draw(self, surface):
        if not self.is_invincible or self.hit_flash_timer % 10 < 5:
            surface.blit(self.current_image, self.rect.topleft)

        for proj in self.projectiles:
            projectile_image = self.images['projectiles'][proj['type']]
            projectile_rect = projectile_image.get_rect(center=(proj['x'], proj['y']))
            surface.blit(projectile_image, projectile_rect)