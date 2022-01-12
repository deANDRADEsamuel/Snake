import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600,600)
PIXEL_SIZE = 10

def collision(pos1, pos2):  #para saber que dois blocos estao na mesma posiçao, estando um egual ao outro
    return pos1 == pos2

  #Pour savoir si le serpent est dans les limits de la fenêtre, 0=X, 1=Y
def off_limits(pos):
    if 0 <=pos[0]< WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True

  #Position pomme
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

  #Creation du programme
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)  #Taille de la fenêtre
pygame.display.set_caption('Snake')

  #Serpent
snake_pos = [(250,50), (260,50), (270,50)]  #Corps du serpent, X,Y, 10 em 10
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))  #Elemento que a gente vai mostrar, superficie que vamos mostrar na tela, quadrade branco
snake_surface.fill((255, 255, 255))  #Couleur blanche
snake_direction = K_LEFT

  #Pomme
apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE)) #Taille
apple_surface.fill((255, 0, 0))  #Couleur rouge
apple_pos = random_on_grid()

  #Quand on meurt, on revient à la case départ
def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250,50), (260,50), (270,50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()
    
  #Pour que le programme ne se ferme pas
while True:
    pygame.time.Clock().tick(15)  #Déplacement
    screen.fill((0, 0, 0))  #background noir
    for event in pygame.event.get():  #Lister tous les événements dans le jeu
        if event.type == QUIT:  #quit = evento saida do jogo, também pode ser escrito pygame.locals.QUIT
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event. key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:  #Pour que seul ces touches là fonctionnent, ex: l'espace ne marcherai pas
                snake_direction = event.key
    
    screen.blit(apple_surface, apple_pos)  #Para aparecer na tela, esta antes da cobra pra a cobra passar por cima da maça e nao o contrario

    if collision(apple_pos, snake_pos[0]):  #en touchant la pomme, le serpent grandit
        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()  #la pote, touchée, réapparait aléatoirement
            
    for pos in snake_pos:
        screen.blit(snake_surface, pos)  #Blit é para desenhar na tela
        
    for i in range(len(snake_pos)-1, 0, -1): #Posiçao (como tamanho) começando da cauda ate a cabeça, pegar na nova peça e igualar la na posiçao da peça interior. 1er numero no py é 0, quer dizer que ultimo elemento de 10 seria 9; o -1 està aqui para nao ter esse problema. Ajuda na fluides quando muda de direçao.
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i-1]
        
        if off_limits(snake_pos[0]):  #Si le serpent touche les bords, Game Over
            restart_game()
            
  #Mouvementation
    if snake_direction == K_UP:
         snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
         snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
         snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
         snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])
        
    pygame.display.update()