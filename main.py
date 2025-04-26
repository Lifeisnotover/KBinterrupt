import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Рогалик с боями")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

PLAYER_SPEED = 5
PLAYER_SIZE = 35
MOB_SIZE = 3
PROJECTILE_SIZE = 8
DOOR_SIZE = 20

player_image = pygame.image.load('character.png')
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))

room_background_image = pygame.image.load('room_background.png')
room_background_image = pygame.transform.scale(room_background_image, (200, 200))

wall_image = pygame.image.load('wall.jpg')
wall_image = pygame.transform.scale(wall_image, (240, 240))

class Room:
    def __init__(self, x, y, w, h, name):
        self.rect = pygame.Rect(x, y, w, h)
        self.name = name
        self.color = (100, 100, 255)
        self.doors = []
        self.mobs = []

    def draw(self, surface, player_rect=None):
        # Draw wall background
        wall_rect = pygame.Rect(self.rect.x - 20, self.rect.y - 20, self.rect.w + 40, self.rect.h + 40)
        surface.blit(wall_image, wall_rect.topleft)

        # Draw room background
        surface.blit(room_background_image, self.rect.topleft)

        # Draw room name
        font = pygame.font.SysFont(None, 24)
        text = font.render(self.name, True, WHITE)
        surface.blit(text, (self.rect.x + 10, self.rect.y + 10))

        # Draw doors
        for door in self.doors:
            color = YELLOW if player_rect and player_rect.colliderect(door['rect']) else GREEN
            pygame.draw.rect(surface, color, door['rect'], 2)

        # Draw mobs
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

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.speed = PLAYER_SPEED
        self.health = 10
        self.projectiles = []
        self.shoot_cooldown = 0

    def draw(self, surface):
        surface.blit(player_image, self.rect.topleft)
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
            closest_mob = None
            min_dist = float('inf')

            for mob in current_room.mobs:
                dist = ((self.rect.centerx - mob['x']) ** 2 + (self.rect.centery - mob['y']) ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    closest_mob = mob

            if closest_mob:
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

class Mob:
    def update_mobs(self, current_room, player):
        for mob in current_room.mobs:
            dx = player.rect.centerx - mob['x']
            dy = player.rect.centery - mob['y']
            length = (dx ** 2 + dy ** 2) ** 0.5
            if length > 0:
                mob['x'] += dx / length * 1
                mob['y'] += dy / length * 1

            if ((mob['x'] - player.rect.centerx) ** 2 + (
                    mob['y'] - player.rect.centery) ** 2) ** 0.5 < PLAYER_SIZE + MOB_SIZE:
                player.health -= 0.1

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

    return [room1, room2, room3, room4, room5]

def show_game_over(screen):
    font = pygame.font.SysFont(None, 72)
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 50))

    font = pygame.font.SysFont(None, 36)
    text = font.render("Нажми R чтобы перезапустить", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 20))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

def main():
    clock = pygame.time.Clock()
    rooms = create_dungeon()
    player = Player(WIDTH // 2, HEIGHT // 2)
    current_room = rooms[0]
    mob_system = Mob()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_e:
                    for door in current_room.doors:
                        if player.rect.colliderect(door['rect']):
                            current_room = door['target']
                            if door['direction'] == 'north':
                                player.rect.bottom = current_room.rect.bottom - 10
                            elif door['direction'] == 'south':
                                player.rect.top = current_room.rect.top + 10
                            elif door['direction'] == 'west':
                                player.rect.right = current_room.rect.right - 10
                            elif door['direction'] == 'east':
                                player.rect.left = current_room.rect.left + 10
                            break

        if player.health <= 0:
            show_game_over(screen)
            rooms = create_dungeon()
            player = Player(WIDTH // 2, HEIGHT // 2)
            current_room = rooms[0]
            continue

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_w]: dy = -player.speed
        if keys[pygame.K_s]: dy = player.speed
        if keys[pygame.K_a]: dx = -player.speed
        if keys[pygame.K_d]: dx = player.speed

        player.move(dx, dy, [current_room])

        if keys[pygame.K_SPACE]:
            player.shoot(current_room)

        player.update_projectiles(current_room)
        mob_system.update_mobs(current_room, player)

        screen.fill(BLACK)
        current_room.draw(screen, player.rect)
        player.draw(screen)

        font = pygame.font.SysFont(None, 30)
        info = [
            f"Комната: {current_room.name}",
            f"Здоровье: {'♥' * int(player.health)}",
        ]
        for i, text in enumerate(info):
            text_surface = font.render(text, True, WHITE)
            screen.blit(text_surface, (10, 10 + i * 30))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
