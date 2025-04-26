import pygame

# Game settings
WIDTH, HEIGHT = 800, 600
PLAYER_SPEED = 5
PLAYER_SIZE = 35
MOB_SIZE = 15  # Увеличиваем размер моба для лучшего отображения изображения
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
        mob_image = pygame.image.load('Images/enemy.png')  # Укажите путь к вашему изображению моба

        player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
        room_background_image = pygame.transform.scale(room_background_image, (200, 200))
        wall_image = pygame.transform.scale(wall_image, (240, 240))
        mob_image = pygame.transform.scale(mob_image, (MOB_SIZE, MOB_SIZE))  # Масштабируем изображение моба

        return {
            'player': player_image,
            'room_bg': room_background_image,
            'wall': wall_image,
            'mob': mob_image  # Добавляем изображение моба в словарь
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None
