import pygame

# Game settings
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
PLAYER_SIZE = 35
MOB_SIZE = 30
PROJECTILE_SIZE = 30  # Увеличиваем размер снаряда для лучшего отображения изображения
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
        mob_image = pygame.image.load('Images/mob.png')  # Укажите путь к вашему изображению моба
        projectile_image_1 = pygame.image.load('Images/one.png')  # Укажите путь к первому изображению снаряда
        projectile_image_2 = pygame.image.load('Images/zero.png')  # Укажите путь к второму изображению снаряда

        player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
        room_background_image = pygame.transform.scale(room_background_image, (200, 200))
        wall_image = pygame.transform.scale(wall_image, (240, 240))
        mob_image = pygame.transform.scale(mob_image, (MOB_SIZE, MOB_SIZE))
        projectile_image_1 = pygame.transform.scale(projectile_image_1, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        projectile_image_2 = pygame.transform.scale(projectile_image_2, (PROJECTILE_SIZE, PROJECTILE_SIZE))

        return {
            'player': player_image,
            'room_bg': room_background_image,
            'wall': wall_image,
            'mob': mob_image,
            'projectile_1': projectile_image_1,
            'projectile_2': projectile_image_2
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None