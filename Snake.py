import pygame
from pygame.locals import *
import random

TAILLE_FENETRE = (600,600)
TAILLE_PIXEL = 10

def collision(pos1, pos2):
    return pos1 == pos2

  #Limites des bords
def off_limits(pos):
    if 0 <=pos[0]< TAILLE_FENETRE[0] and 0 <= pos[1] < TAILLE_FENETRE[1]:
        return False
    else:
        return True

  #Position pomme
def random_on_grid():
    x = random.randint(0, TAILLE_FENETRE[0])
    y = random.randint(0, TAILLE_FENETRE[1])
    return x // TAILLE_PIXEL* TAILLE_PIXEL, y // TAILLE_PIXEL * TAILLE_PIXEL

  #Creation du programme
pygame.init()
screen = pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption('Snake')

  #Serpent
snake_pos = [(250,50), (260,50), (270,50)]
snake_surface = pygame.Surface((TAILLE_PIXEL, TAILLE_PIXEL))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

  #Pomme
pomme_surface = pygame.Surface((TAILLE_PIXEL, TAILLE_PIXEL))
pomme_surface.fill((255, 0, 0))
pomme_pos = random_on_grid()

  #En mourant, le jeu recommence
def restart_game():
    global snake_pos
    global pomme_pos
    global snake_direction
    snake_pos = [(250,50), (260,50), (270,50)]
    snake_direction = K_LEFT
    pomme_pos = random_on_grid()
    
  #Pour que le programme ne se ferme pas
while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event. key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key
    
    screen.blit(pomme_surface, pomme_pos)  #La pomme apparaît sur l'écran

    if collision(pomme_pos, snake_pos[0]):  #en touchant la pomme, le serpent grandit
        snake_pos.append((-10, -10))
        pomme_pos = random_on_grid()  #la pomme, touchée, réapparait aléatoirement
            
    for pos in snake_pos:
        screen.blit(snake_surface, pos)
        
    for i in range(len(snake_pos)-1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            restart_game()
        snake_pos[i] = snake_pos[i-1]
        
        if off_limits(snake_pos[0]):  #Si le serpent touche les bords, Game Over
            restart_game()
            
  #Mouvementation
    if snake_direction == K_UP:
         snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - TAILLE_PIXEL)
    elif snake_direction == K_DOWN:
         snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + TAILLE_PIXEL)
    elif snake_direction == K_LEFT:
         snake_pos[0] = (snake_pos[0][0] - TAILLE_PIXEL, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
         snake_pos[0] = (snake_pos[0][0] + TAILLE_PIXEL, snake_pos[0][1])
        
    pygame.display.update()
