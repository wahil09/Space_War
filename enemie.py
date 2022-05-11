import pygame
from person import Person

class Enemei(Person):
    def __init__(self, name, age, health, damage, velocity, position, image, size_img):
        super().__init__(name, age, health, damage, velocity, position, image, size_img)

    def draw(self, win, tail_win):
        return win.blit(self.image, (self.rect.x, self.rect.y))

    def movement(self, delta, size_win):
        self.rect.y += (self.get_velocity()-self.get_velocity()/2)*delta
        if self.rect.x < size_win[0]:
            self.rect.x += self.get_velocity()*delta
        else:
            self.rect.x = -70
