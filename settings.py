import pygame
pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

WIDTH = int(SCREEN_WIDTH)
HEIGHT = int(SCREEN_HEIGHT)

PLAYER_SPEED = HEIGHT// 400
PLAYER_SIZE = HEIGHT // 12
MOB_SIZE = HEIGHT // 15
DOOR_SIZE = 20
MOB_SPEED = 1
INVINCIBILITY_DURATION = 60
MOB_DAMAGE = 1
FONT_SIZE = 32

PROJECTILE_SIZE = HEIGHT // 20
PROJECTILE_SPEED = HEIGHT // 100
SHOOT_DELAY = 1000

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
        idle_images = [pygame.image.load('Images/idle_right_1.png'), pygame.image.load('Images/idle_right_2.png')]
        up_image = pygame.image.load('Images/up.png')
        down_images = [pygame.image.load('Images/down.png')]

        room_background_image = pygame.image.load('Images/room_background.png')
        wall_image = pygame.image.load('Images/wall.jpg')
        mob_image = pygame.image.load('Images/mob.png')
        projectile_image_1 = pygame.image.load('Images/one.png')
        projectile_image_2 = pygame.image.load('Images/zero.png')


        idle_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in idle_images]
        right_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in right_images]
        left_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in left_images]
        up_image = [pygame.transform.scale(up_image, (PLAYER_SIZE, PLAYER_SIZE))]
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
            'idle_right': idle_images,
            'projectiles': {
                '0': projectile_image_1,
                '1': projectile_image_2
            }
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None
