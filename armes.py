import time
import pygame

class Arms(pygame.sprite.Sprite):
    number_of_fire = 0
    def __init__(self, name, damage, image, animation, velocity, person_position, constructor):
        super().__init__()
        self.name = name
        self.damage = damage
        self.image = pygame.image.load(image)
        self.animation = animation
        self.velocity = velocity
        self.__damage = damage
        self.constructor = constructor
        self.image = self.transform(image, (20, 45))
        self.animation = animation
        self.rect = self.image.get_rect()
        self.person_position = person_position
        self.rect.x, self.rect.y = self.person_position.get_position()[0]-self.get_size()[0]/2+self.person_position.get_size()[0]/2, self.person_position.get_position()[1]+self.get_size()[1]
        self.premier_position = 0
        self.delta = 0
        self.time_passe = time.time()
        self.time_pour_tirer = 0.1
        Arms.number_of_fire += 1



    def get_size(self):
        return self.image.get_size()

    def attack_target(self, target):
        target.get_attack(self.constructor.player)
        self.remove()

    def lancer_attack(self, delta):
        self.rect.y += self.velocity*delta
        if self.rect.y > 1050: #height de window
            self.remove()

    def remove(self):
        self.constructor.all_enemie_fire.remove(self)

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_number_of_fire(self):
        return Arms.number_of_fire

    # transfor l'image
    def transform(self, image, new_size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, new_size)
        return self.image

    def get_damage(self):
        return self.__damage
