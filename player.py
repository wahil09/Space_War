from person import Person
import pygame


class Player(Person):
    def __init__(self, name, age, health, damage, velocity, position, image, size_img, constructor):
        super().__init__(name, age, health, damage, velocity, position, image, size_img, constructor)
        self.__kill = 0


    def enemie_touch_player(self):
        for enemie in self.constructor.check_collision(self, self.constructor.all_enemie):
            self.get_attack(enemie)
            enemie.remove()
    def draw(self, win, jeu):
        self.calcul_pos_player((win.get_width(), win.get_height()))
        self.test_self_alive() # tester si la vie de joueur est plus de 0 sinon met 'is_alive' a False

        self.enemie_touch_player()
        if not self.is_alive:
            jeu.jeu_active = self.is_alive

        return win.blit(self.image, (self.rect.x, self.rect.y))

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
















