import time

import pygame
from fire import Fire

class Person(pygame.sprite.Sprite):
    gravity = -9.8
    number_of_person = 0

    def __init__(self, name, age, health, damage, velocity, position, image, size_img):
        super().__init__()
        self.__name = name
        self.__age = age
        self.__health = health
        self.__max_health = self.__health
        self.__damage = damage
        self.__velocity = velocity
        self.__jumb = 10
        self.image = self.transform(image, size_img)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position
        self.delta = 1

        self.premier_position = 0

        self.time_passe = time.time()


        Person.number_of_person += 1

    # ***** -- Getters Functions -- ***** #
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_image(self):
        return self.image

    def get_health(self):
        return self.__health

    def get_damage(self):
        return self.__damage

    def get_velocity(self):
        return self.__velocity

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_size(self):
        return self.image.get_size()

    def get_max_health(self):
        return self.__max_health

    def get_attack(self, enemie):
        self.__health -= enemie.get_damage()

    def get_damage_arm(self, arm):
        self.__damage = arm.get_damage()


    # ***** -- Setters Functions -- ***** #

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age

    def set_image(self, new_image):
        self.image = new_image

    def set_health(self, new_health):
        self.__health = new_health

    def set_damage(self, new_damage):
        self.__damage = new_damage

    def set_velocity(self, new_velocity):
        self.__velocity = new_velocity


    # ***** -- Movement -- ***** #

    def move_left(self, btn_clicked, delta):
        if btn_clicked:

            self.rect.x -= self.__velocity * delta

    def move_right(self, btn_clicked, delta):
        if btn_clicked:
            self.rect.x += self.__velocity * delta

    def move_up(self, btn_clicked, delta):
        if btn_clicked:
            self.rect.y -= self.__velocity * delta

    def move_down(self, btn_clicked, delta):
        if btn_clicked:
            self.rect.y += self.__velocity * delta


    # Tirer
    def lancer_fire(self, fire, btn_clicked, delta, win):
        pass



    # Dessiner les caractères de jeux

    def calcul_pos_player(self, tail_win):
        if self.premier_position < 1:
            self.rect.x = tail_win[0]/2-self.image.get_width()/2
            self.rect.y = tail_win[1]-self.image.get_width()
            self.premier_position += 1

    def draw(self, win, tail_win):
        self.calcul_pos_player(tail_win)
        return win.blit(self.image, (self.rect.x, self.rect.y))

    def get_delta(self, delta):
        return delta


    # transfor l'image
    def transform(self, image, new_size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, new_size)
        return self.image


    # bar Health
    def draw_health_bar(self, surface):
        bg_color = (111, 210, 46)
        back_color = (000, 000, 000)
        position = [self.rect.x+4, self.rect.y-12, self.__health, 5]
        back_position = [self.rect.x + 4, self.rect.y -12, self.__max_health, 5]
        pygame.draw.rect(surface, back_color, back_position)
        pygame.draw.rect(surface, bg_color, position)

    def delay(self):
        pass


