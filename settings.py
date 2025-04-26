import pygame

# Game settings
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
PLAYER_SIZE = 35
MOB_SIZE = 3
PROJECTILE_SIZE = 8
DOOR_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)


def load_images():
    try:
        player_image = pygame.image.load('Images/character.png')
        room_background_image = pygame.image.load('Images/room_background.png')
        wall_image = pygame.image.load('Images/wall.jpg')

        player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
        room_background_image = pygame.transform.scale(room_background_image, (200, 200))
        wall_image = pygame.transform.scale(wall_image, (240, 240))

        return {
            'player': player_image,
            'room_bg': room_background_image,
            'wall': wall_image
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None