import pygame
from player import Player
from enemie import Enemei
from fire import Fire
import random
class Constructor:
    def __init__(self):
        self.player = Player('wahil', 19, 100, 14, 300, (0, 0), 'public/images/Player/Spaceships/01/Spaceship_01_BLUE.png', (150, 100))
        self.all_enemie = []
        self.all_fire = []
        self.pressed = {}

    def creer_fire(self):
        self.fire = Fire(self.player)
        self.all_fire.append(self.fire)

    def creer_enemei(self):
        self.enemie = Enemei('lvl1', 15, 60, 5, random.randint(80, 150), (random.randint(50, 1000), 50), 'public/images/enemie/1B.png', (120, 80))
        self.all_enemie.append(self.enemie)

    def sup_fire(self):
        self.all_fire.pop(0)










