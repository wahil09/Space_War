import pygame
from player import Player
from enemie import Enemei
from fire import Fire
import random
class Constructor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = Player('wahil', 19, 100, 0, 400, (0, 0), 'public/images/Player/Spaceships/01/Spaceship_01_BLUE.png', (150, 100))
        self.all_enemie = pygame.sprite.Group()
        self.all_fire = pygame.sprite.Group()
        self.pressed = {}

    def creer_fire(self):
        self.fire = Fire(self.player, self)
        self.all_fire.add(self.fire)

    def creer_enemei(self):
        self.enemie = Enemei('lvl1', 15, 100, 10, 80, (random.randint(100, 900), -10), 'public/images/enemie/1B.png', (100, 60), self)
        self.all_enemie.add(self.enemie)

    def check_collision(self, qui_touche, group_target):
        return pygame.sprite.spritecollide(qui_touche, group_target, False, pygame.sprite.collide_mask)















