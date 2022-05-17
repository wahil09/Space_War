import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, txt_button, surface, color, position, dimension, btn_image):
        super().__init__()
        self.txt_button = txt_button
        self.surface = surface
        self.color = color
        self.position = position
        self.dimension = dimension
        self.txt_button = txt_button
        self.image = self.transform(btn_image, self.dimension)
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]-self.image.get_width()/2
        self.rect.y = self.position[1]-self.image.get_height()*2.5

    def get_txt(self):
        return self.txt_button

    # transfor l'image
    def transform(self, image, new_size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, new_size)
        return self.image

    def click_mouse(self, mouse_clicked, mouse_position):
        mouse_sur_btn = mouse_position[0] >= self.rect.left and mouse_position[0] <= self.rect.right and mouse_position[1] >= self.rect.top and mouse_position[1] <= self.rect.bottom
        if mouse_sur_btn and mouse_clicked:
            return self.get_txt()
        elif mouse_sur_btn:
            pass

