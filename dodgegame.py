## Importation des librairies necessaires
import pygame
import random
import math

## Initialisation de pygame
pygame.init()

largeur_ecran = 880
hauteur_ecran = 600
couleur_1 = (51,204,204)
couleur_2 = (0,0,0)
couleur_3 = (255, 0, 0)
display = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Dodge Cube avec Pygame")
f_rate = pygame.time.Clock()
detail_joueur = 45
mvm_joueur = [largeur_ecran // 2, hauteur_ecran - 2 * detail_joueur]

vitesse_joueur = 15
detail_jeu = 45
position_1 = [random.randint(0, largeur_ecran - detail_jeu), 0]
position_2 = [random.randint(0, largeur_ecran - detail_jeu), 0]
vitesse_jeu_d = 10
points = 0
font = pygame.font.SysFont("calibri", 35)

def check_for_colision(mvm_joueur, enemy_pos):
    p_x, p_y = mvm_joueur
    e_x, e_y = enemy_pos
    if (e_x < p_x < e_x + detail_jeu or e_x < p_x + detail_joueur < e_x + detail_jeu) and \
            (e_y < p_y < e_y + detail_jeu or e_y < p_y + detail_joueur < e_y + detail_jeu):
        return True
    return False

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mvm_joueur[0] -= vitesse_joueur
    if keys[pygame.K_RIGHT]:
        mvm_joueur[0] += vitesse_joueur
    if mvm_joueur[0] < 0:
        mvm_joueur[0] = 0
    elif mvm_joueur[0] > largeur_ecran - detail_joueur:
        mvm_joueur[0] = largeur_ecran - detail_joueur
    display.fill(couleur_2)
    position_1[1] += vitesse_jeu_d
    position_2[1] += vitesse_jeu_d
    if position_1[1] > hauteur_ecran:
        position_1 = [random.randint(0, largeur_ecran - detail_jeu), 0]
        points += 1  
        vitesse_jeu_d += 0.5 
    if position_2[1] > hauteur_ecran:
        position_2 = [random.randint(0, largeur_ecran - detail_jeu), 0]
        points += 1  
        vitesse_jeu_d += 0.5 
    if check_for_colision(mvm_joueur, position_1) or check_for_colision(mvm_joueur,
                                                                                   position_2):
        game_over = True
        break
    pygame.draw.rect(display, couleur_3, (position_1[0], position_1[1],
                                       detail_jeu, detail_jeu))
    pygame.draw.rect(display, couleur_3, (position_2[0], position_2[1], 
                                       detail_jeu, detail_jeu))
    pygame.draw.rect(display, couleur_1, (mvm_joueur[0], mvm_joueur[1],
                                       detail_joueur, detail_joueur))
    score_text = font.render("Score: {}".format(points), True, couleur_1)
    display.blit(score_text, (10, 10))
    pygame.display.update()
    f_rate.tick(30)

display.fill(couleur_2)
game_over_text = font.render("Final Score: {}".format(points), True, couleur_1)
display.blit(game_over_text, (largeur_ecran // 2 - 200, hauteur_ecran // 2 - 20))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()