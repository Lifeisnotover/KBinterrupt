from KBinterrupt.settings import *

class Mob:
    def update_mobs(self, current_room, player):
        for mob in current_room.mobs:
            dx = player.rect.centerx - mob['x']
            dy = player.rect.centery - mob['y']
            length = (dx**2 + dy**2)**0.5
            if length > 0:
                mob['x'] += dx/length * 1
                mob['y'] += dy/length * 1

            if ((mob['x'] - player.rect.centerx)**2 +
                (mob['y'] - player.rect.centery)**2)**0.5 < PLAYER_SIZE + MOB_SIZE:
                player.health -= 0.1