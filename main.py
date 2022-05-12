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
        self.enemie_par_second = 1.5 # seconde
        self.fire_par_second = 0.3 # seconde

        self.jeu_active = True


    def draw(self):

        while self.jeu_active:
            print(player.get_number_of_kill())
            # Calcul delta time
            time_actuel = time.time()
            self.delta = time_actuel - self.time_passe
            self.time_passe = time_actuel

            # time pour creer un enemie
            self.delta_2 = time_actuel - self.time_passe_2

            if self.delta_2 > self.enemie_par_second:
                model.creer_enemei()
                self.enemie_par_second = self.delta_2 + 1.5


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
            player.move_right(model.pressed.get(pygame.K_RIGHT), self.delta)
            player.move_up(model.pressed.get(pygame.K_UP), self.delta)
            player.move_down(model.pressed.get(pygame.K_DOWN), self.delta)

            # Dessiner le window
            self.win.blit(self.bg, (0, 0))

            # Afficher le joueur
            player.draw(self.win, (self.width, self.height))
            player.draw_health_bar(self.win)

            # Afficher Fire attack
            global fire
            for fire in fires:
                fire.lancer_attack(self.delta)
                if model.pressed.get(pygame.K_SPACE): # si en tire le fire pas un autre attaque
                    player.get_damage_arm(fire)
            model.all_fire.draw(self.win)


            # Aficher les enemie lvl-01
            for enemie in model.all_enemie:
                enemie.draw_health_bar(self.win)
                enemie.movement(self.delta, (self.width, self.height))
                #fire.attack_target(enemie)
            model.all_enemie.draw(self.win)

            if model.pressed.get(pygame.K_SPACE):
                if self.delta_2 > self.fire_par_second:
                    model.creer_fire()
                    self.fire_par_second = self.delta_2 + 0.3

            # pygame.draw.rect(win, "#ffffff", (player.get_position(), player.get_size())) mettre une couleur blanche sur le player


            # get delta time
            player.get_delta(self.delta)
            pygame.display.update()
            self.clock.tick(self.FPS)  # 60 FPS
        pygame.quit()


if __name__ == '__main__':
    game = Window()
    game.draw()

