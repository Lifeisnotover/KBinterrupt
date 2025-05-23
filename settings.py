import pygame

pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h

WIDTH = int(SCREEN_WIDTH)
HEIGHT = int(SCREEN_HEIGHT)

PLAYER_SPEED = HEIGHT // 400
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

HEART_SIZE = 30
HEART_SPACING = 5
TEXT_OFFSET = 10

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
MAX_HEALTH = 15


def load_images2():
    try:
        right_images = [pygame.image.load('Images/right_right.png'), pygame.image.load('Images/right_left.png')]
        left_images = [pygame.image.load('Images/left_right.png'), pygame.image.load('Images/left_left.png')]
        up_image = pygame.image.load('Images/up.png')
        down_images = [pygame.image.load('Images/down.png')]
        roomback2 = pygame.image.load('Images/floor.png')
        wlls2 = pygame.image.load('Images/stens.jpg')
        mob_image = pygame.image.load('Images/mob.png')
        projectile_image_1 = pygame.image.load('Images/one.png')
        projectile_image_2 = pygame.image.load('Images/zero.png')
        stares_image = pygame.image.load('Images/Staries.png')
        idle_images = [pygame.image.load('Images/idle_right_1.png'), pygame.image.load('Images/idle_right_2.png')]
        boss = pygame.image.load('Images/Untitled 04-27-2025 02-22-04.png')
        boss = pygame.transform.scale(boss, (300, 300))
        right_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in right_images]
        left_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in left_images]
        up_image = [pygame.transform.scale(up_image, (PLAYER_SIZE, PLAYER_SIZE))]
        down_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in down_images]
        projectile_image_1 = pygame.transform.scale(projectile_image_1, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        projectile_image_2 = pygame.transform.scale(projectile_image_2, (PROJECTILE_SIZE, PROJECTILE_SIZE))
        idle_images = [pygame.transform.scale(img, (PLAYER_SIZE, PLAYER_SIZE)) for img in idle_images]
        return {
            'right': right_images,
            'left': left_images,
            'up': up_image,
            'down': down_images,
            'room_bg': roomback2,
            'wall': wlls2,
            'mob': mob_image,
            'projectiles': {
                '0': projectile_image_1,
                '1': projectile_image_2
            },
            'idle_right': idle_images,
            'boss': boss
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None


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
        stares_image = pygame.image.load('Images/Staries.png')

        heart_image = pygame.image.load('Images/heart.png')
        empty_heart_image = pygame.image.load('Images/empty_heart.png')

        heart_images = [pygame.transform.scale(heart_image, (HEART_SIZE, HEART_SIZE))]
        empty_heart_images = [pygame.transform.scale(empty_heart_image, (HEART_SIZE, HEART_SIZE))]

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
            'heart': heart_images,
            'empty_heart': empty_heart_images,
            'projectiles': {
                '0': projectile_image_1,
                '1': projectile_image_2
            },
            'stairs': stares_image
        }
    except Exception as e:
        print(f"Ошибка загрузки изображений: {e}")
        return None
