import pygame

class Arms:
    def __int__(self, name, damage, image, animation, velocity, position):
        self.name = name
        self.damage = damage
        self.image = pygame.image.load(image)
        self.animation = animation
        self.velocity = velocity
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

