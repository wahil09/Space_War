import pygame, random, time
from constructor import Constructor
pygame.init()


model = Constructor()
player = model.player

fires = model.all_fire

class Window:
    def __init__(self):
        self.width, self.height = 1024, 1024 #
        self.random_bg = random.randint(1, 7) # choisir un numero aléatoire pour le background de jeux
        self.bg = pygame.image.load(f'public/images/Background/Starfields/Starfield-{self.random_bg}.png')
        self.title = pygame.display.set_caption('Space_War-war')
        self.win = pygame.display.set_mode((self.width, self.height))
        self.delta = 0
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.time_passe = time.time()
        self.time_passe_2 = time.time()
        self.delta_2 = 0
        self.enemie_par_second = 3 # Male nommer le variable
        self.time_entre_chaque_enemie = 0 # seconde # Male nommer le variable
        self.fire_par_second = 0.2 # seconde # Male nommer le variable
        self.jeu_active = True

        self.vag = 1
        self.enemie_par_vag = 10
    def prochain_vag(self, number_of_kill):
        if number_of_kill >= self.enemie_par_vag:
            self.enemie_par_vag += 10
            self.vag += 1
            if self.enemie_par_second > 1:
                self.enemie_par_second -= random.choice([0.2, 0.4])

        if self.vag == 5:
            # model.appeler_bos()
            pass

    def draw_number_of_vag(self):
        font = pygame.font.Font('public/font/Macondo-Regular.ttf', 25)
        vag_txt = pygame.font.Font.render(font, f"Vag: {self.vag}", False, 'white')
        self.win.blit(vag_txt, (self.win.get_width()/2-vag_txt.get_width()/2, 20))


    def draw(self):
        while self.jeu_active:
            # Dessiner le window
            self.win.blit(self.bg, (0, 0))

            # Systeme de niveau
            self.prochain_vag(player.get_number_of_kill())
            self.draw_number_of_vag()

            # Calcul delta time
            time_actuel = time.time()
            self.delta = time_actuel - self.time_passe
            self.time_passe = time_actuel

            # time pour creer un enemie
            self.delta_2 = time_actuel - self.time_passe_2

            if self.delta_2 > self.time_entre_chaque_enemie:
                model.creer_enemei()
                self.time_entre_chaque_enemie = self.delta_2 + self.enemie_par_second


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jeu_active = False

                # Touche Keyboard
                if event.type == pygame.KEYDOWN:
                    model.pressed[event.key] = True

                if event.type == pygame.KEYUP:
                    model.pressed[event.key] = False

            # Movement player
            player.move_left(model.pressed.get(pygame.K_LEFT), self.delta)
            player.move_right(model.pressed.get(pygame.K_RIGHT), self.delta, self.win)
            player.move_up(model.pressed.get(pygame.K_UP), self.delta)
            player.move_down(model.pressed.get(pygame.K_DOWN), self.delta, self.win)


            # Afficher le joueur
            player.draw(self.win, self)
            player.draw_health_bar(self.win)
            player.draw_number_of_kill_enemie(self.win)

            # Afficher Fire attack
            model.all_fire.draw(self.win)
            for fire in fires:
                fire.lancer_attack(self.delta)
                if model.pressed.get(pygame.K_SPACE): # si en tire le fire pas un autre attaque
                    player.get_damage_arm(fire)


            # Aficher les enemie lvl-01
            model.all_enemie.draw(self.win)
            for enemie in model.all_enemie:
                enemie.draw_health_bar(self.win)
                enemie.movement(self.delta, (self.width, self.height), time_actuel)



            # Afficher l'attaque le l'enemie
            model.all_enemie_fire.draw(self.win)
            for enemie_fire in model.all_enemie_fire:
                enemie_fire.lancer_attack(self.delta)

            if model.pressed.get(pygame.K_SPACE):
                if self.delta_2 > self.fire_par_second:
                    model.creer_fire()
                    self.fire_par_second = self.delta_2 + 0.2

            # pygame.draw.rect(win, "#ffffff", (player.get_position(), player.get_size())) mettre une couleur blanche sur le player


            # get delta time
            player.get_delta(self.delta)
            pygame.display.update()
            self.clock.tick(self.FPS)  # 60 FPS
        pygame.quit()


if __name__ == '__main__':
    game = Window()
    game.draw()

