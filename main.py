import pygame, random, time
from constructor import Constructor
pygame.init()


model = Constructor()
player = model.player

fires = model.all_fire

# Créer et afficher les enemie lvl-01


WIDTH, HEIGHT = 1024, 1024
rndm = random.randint(1, 7)
bg = pygame.image.load(f'public/images/Background/Starfields/Starfield-{rndm}.png')

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space_War-war')
clock = pygame.time.Clock()
FPS = 60

delta = 0
time_passer = time.time()



start_time = time.time()
delay_cree_enemie = 1

delay_cree_fire = 0.5
def main():
    global time_passer, delay_cree_enemie, delay_cree_fire
    is_start = True

    while is_start:
        # Calcul delta time
        time_actuel = time.time()
        delta = time_actuel - time_passer
        print(time_actuel, time_passer, delta)

        # time pour creer un enemie
        diference_time_actuel_passer = time_actuel - start_time

        if diference_time_actuel_passer > delay_cree_enemie:
            model.creer_enemei()
            delay_cree_enemie = diference_time_actuel_passer + 1.5

        time_passer = time_actuel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_start = False

            # Touche Keyboard
            if event.type == pygame.KEYDOWN:
                model.pressed[event.key] = True

            if event.type == pygame.KEYUP:
                model.pressed[event.key] = False

        # Movement player
        player.move_left(model.pressed.get(pygame.K_LEFT), delta)
        player.move_right(model.pressed.get(pygame.K_RIGHT), delta)
        player.move_up(model.pressed.get(pygame.K_UP), delta)
        player.move_down(model.pressed.get(pygame.K_DOWN), delta)

        # Dessiner le window
        win.blit(bg, (0, 0))

        # Afficher le joueur
        player.draw(win, (WIDTH, HEIGHT))

        # Afficher Fire attack
        for fire in fires:
            fire.draw(win, delta)
            if fire.get_position()[1] < -10:
                model.sup_fire()
            print(fire.get_position())

        if model.pressed.get(pygame.K_SPACE):
            if diference_time_actuel_passer > delay_cree_fire:
                model.creer_fire()
                delay_cree_fire = diference_time_actuel_passer + 0.5

        # pygame.draw.rect(win, "#ffffff", (player.get_position(), player.get_size())) mettre une couleur blanche sur le player


        # fficher les enemie lvl-01
        for enemie in model.all_enemie:
            enemie.draw(win, (WIDTH, HEIGHT))
            enemie.movement(delta, (WIDTH, HEIGHT))
        # get delta time
        player.get_delta(delta)
        pygame.display.update()
        clock.tick(FPS) #60 FPS
    pygame.quit()
if __name__ == '__main__':
    main()











