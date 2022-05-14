from person import Person
import pygame


class Player(Person):
    def __init__(self, name, age, health, damage, velocity, position, image, size_img, constructor):
        super().__init__(name, age, health, damage, velocity, position, image, size_img, constructor)
        self.__kill = 0

    # bar Health
    def draw_health_bar(self, surface):
        bg_color = (111, 210, 46)
        back_color = (111, 111, 111)
        position = [10, 30, self.get_health()*2, 15]
        back_position = [10, 30, self.get_max_health()*2, 15]
        pygame.draw.rect(surface, back_color, back_position)
        pygame.draw.rect(surface, bg_color, position)

    def get_number_of_kill(self):
        return self.__kill

    def add_number_of_kill(self):
        self.__kill += 1

    def draw_number_of_kill_enemie(self, win):
        font = pygame.font.Font('public/font/Macondo-Regular.ttf', 35)
        kill_txt = pygame.font.Font.render(font, f"Kill: {self.get_number_of_kill()}", True, 'white')
        win.blit(kill_txt, (win.get_width()-kill_txt.get_width()*1.2, 20))
















