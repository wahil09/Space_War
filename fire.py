import time
import pygame

class Fire(pygame.sprite.Sprite):
    number_of_fire = 0
    def __init__(self, player, constructor):
        super().__init__()
        self.__damage = 25
        self.constructor = constructor
        self.name = 'fire'
        self.velocity = 1000
        self.image = self.transform('public/images/Player/Flame_01.png', (20, 45))
        self.animation = 'animation'
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x, self.rect.y = self.player.get_position()[0]-self.get_size()[0]/2+self.player.get_size()[0]/2, self.player.get_position()[1]-self.get_size()[1]
        self.premier_position = 0
        self.delta = 0
        self.time_passe = time.time()
        self.time_pour_sup = 0.1
        Fire.number_of_fire += 1


    def get_size(self):
        return self.image.get_size()

    def attack_target(self, target):
        target.get_attack(self.constructor.player)
        self.remove()

    def lancer_attack(self, delta):
        self.rect.y -= self.velocity*delta
        if self.rect.y < -30:
            self.remove()
        for enemie in self.constructor.check_collision(self, self.constructor.all_enemie):
            self.remove()
            enemie.get_attack(self)


    def remove(self):
        self.constructor.all_fire.remove(self)

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_number_of_fire(self):
        return Fire.number_of_fire

    # transfor l'image
    def transform(self, image, new_size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, new_size)
        return self.image

    def get_damage(self):
        return self.__damage
