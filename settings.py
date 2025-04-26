import pygame
# Game settings
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
PLAYER_SIZE = 40
MOB_SIZE = 30
PROJECTILE_SIZE = 8
DOOR_SIZE = 20

# Puzzle settings
PUZZLE_WIDTH = 800
PUZZLE_HEIGHT = 600
FONT_SIZE = 32

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)

def load_images():
    try:
        right_images = [pygame.image.load('Images/right_right.png'), pygame.image.load('Images/right_left.png')]
        left_images = [pygame.image.load('Images/left_right.png'), pygame.image.load('Images/left_left.png')]
        up_image = pygame.image.load('Images/up.png')
        down_images = [pygame.image.load('Images/down.png')]

        room_background_image = pygame.image.load('Images/room_background.png')
        wall_image = pygame.image.load('Images/wall.jpg')
        mob_image = pygame.image.load('Images/mob.png')
        projectile_image_1 = pygame.image.load('Images/one.png')
        projectile_image_2 = pygame.image.load('Images/zero.png')

        right_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in right_images]
        left_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in left_images]
        up_image = pygame.transform.scale(up_image, (PLAYER_SIZE, PLAYER_SIZE))
        down_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in down_images]
        room_background_image = pygame.transform.scale(room_background_image, (200, 200))
        wall_image = pygame.transform.scale(wall_image, (240, 240))
        mob_image = pygame.transform.scale(mob_image, (MOB_SIZE, MOB_SIZE))
        projectile_image_1 = pygame.transform.scale(projectile_image_1, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        projectile_image_2 = pygame.transform.scale(projectile_image_2, (PROJECTILE_SIZE, PROJECTILE_SIZE))

        return {
            'right': right_images,
            'left': left_images,
            'up': up_image,
            'down': down_images,
            'room_bg': room_background_image,
            'wall': wall_image,
            'mob': mob_image,
            'projectiles': {
                '0': projectile_image_1,
                '1': projectile_image_2
            }
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None