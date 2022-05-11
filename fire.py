import pygame

class Fire:
    number_of_fire = 0
    def __init__(self, player):
        self.name = 'fire'
        self.damage = 10
        self.velocity = 450
        self.image = self.transform('public/images/Player/Flame_01.png', (25, 50))
        self.animation = 'animation'
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x, self.rect.y = self.player.get_position()[0]-self.get_size()[0]/2+self.player.get_size()[0]/2, self.player.get_position()[1]-self.get_size()[1]

        self.remier_position = 0
        Fire.number_of_fire += 1


    def get_size(self):
        return self.image.get_size()

    def lancer_attack(self, delta):
        self.rect.y -= self.velocity*delta


    def draw(self, win, delta):
        self.lancer_attack(delta)
        win.blit(self.image, (self.rect.x, self.rect.y))

        print({"Fire_X": self.rect.x, "Fire_Y": self.rect.y})

    def get_position(self):
        return self.rect.x, self.rect.y

    def get_number_of_fire(self):
        return Fire.number_of_fire

    # transfor l'image
    def transform(self, image, new_size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, new_size)
        return self.image