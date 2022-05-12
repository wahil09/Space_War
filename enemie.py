import pygame
from person import Person


class Enemei(Person, pygame.sprite.Sprite):
    def __init__(self, name, age, health, damage, velocity, position, image, size_img, constructor):
        super().__init__(name, age, health, damage, velocity, position, image, size_img)
        self.constructor = constructor

    def movement(self, delta, size_win):
        self.rect.y += abs(self.get_velocity() * delta)
        self.rect.x += (self.get_velocity()*2) * delta

        if self.rect.x == size_win[0]-self.image.get_width():
            self.set_velocity(-self.get_velocity())

        if self.rect.x < 0:
            self.set_velocity(abs((self.get_velocity()*1.4)))

        if self.constructor.check_collision(self, self.constructor.all_fire):
            self.get_attack(self.constructor.player)


        if self.rect.y > 1000 or self.get_health() <= 0:
            self.constructor.player.add_number_of_kill()
            self.remove()

    def remove(self):
        self.constructor.all_enemie.remove(self)




"""    def draw(self, win, tail_win):
        return win.blit(self.image, (self.rect.x, self.rect.y))
"""
