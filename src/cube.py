## Importation des librairies necessaires
import pygame
import random
import math
import time

## Initialisation de pygame
pygame.init()
## Configuration de l'affichage et autres parametres du jeu
largeur_ecran = 600
hauteur_ecran = 800
cube_col = (0,200,0)
fond_jeu = (0,0,0)
finjeu = (255,255,0)
cube_enemy = (255, 0, 0)
display = pygame.display.set_mode((largeur_ecran, hauteur_ecran))
pygame.display.set_caption("Dodge Cube avec pygame")
f_rate = pygame.time.Clock()
detail_joueur = 45
mvm_joueur = [largeur_ecran // 2, hauteur_ecran - 2 * detail_joueur]

vitesse_joueur = 15
detail_jeu = 45
position_1 = [random.randint(0, largeur_ecran - detail_jeu), 0]
position_2 = [random.randint(0, largeur_ecran - detail_jeu), 0]
vitesse_jeu_d = 10
points = 0
font = pygame.font.SysFont("calibri", 25)

## Fonctions gerant la collision avec les coordonnées des cubes
def collision(mvm_joueur, enemy_pos):
    JoueurX, JoueurY = mvm_joueur
    EnemyX, EnemyY = enemy_pos
    if (EnemyX < JoueurX < EnemyX + detail_jeu or EnemyX < JoueurX + detail_joueur < EnemyX + detail_jeu) and \
            (EnemyY < JoueurY < EnemyY + detail_jeu or EnemyY < JoueurY + detail_joueur < EnemyY + detail_jeu):
        return True
    return False
## Initialisation de la variable d'arret du jeu
game_over = False

## Detection de la touche de direction gauche    
def touche_gauche(cle):
    if cle[pygame.K_LEFT]:
        mvm_joueur[0] -= vitesse_joueur

## Detection de la touche de direction gauche 
def touche_droite(cle):
    if cle[pygame.K_RIGHT]:
        mvm_joueur[0] += vitesse_joueur

## Creation de la fenetre du jeu
def fenetre(Mygame):
    Mygame.draw.rect(display, cube_enemy, (position_1[0], position_1[1],detail_jeu, detail_jeu))
    Mygame.draw.rect(display, cube_enemy, (position_2[0], position_2[1],detail_jeu, detail_jeu))
    Mygame.draw.rect(display, cube_col, (mvm_joueur[0], mvm_joueur[1],detail_joueur, detail_joueur))
    score_tEnemyXt = font.render("Score: {}".format(points), True, cube_col)
    display.blit(score_tEnemyXt, (10, 10))
    Mygame.display.update()
    f_rate.tick(30)

## Debut du jeu
if __name__ == "__main__" :
    # jeuCube(pygame)
    while not game_over:
        keys = pygame.key.get_pressed()
        ## Faire quitter le jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        touche_gauche(keys)
        touche_droite(keys)
        if mvm_joueur[0] < 0:
            mvm_joueur[0] = 0
        elif mvm_joueur[0] > largeur_ecran - detail_joueur:
            mvm_joueur[0] = largeur_ecran - detail_joueur
        display.fill(fond_jeu)
        position_1[1] += vitesse_jeu_d
        position_2[1] += vitesse_jeu_d
        if position_1[1] > hauteur_ecran:
            position_1 = [random.randint(0, largeur_ecran - detail_jeu), 0]
            points += 1  
            vitesse_jeu_d += 0.25 

        if position_2[1] > hauteur_ecran:
            position_2 = [random.randint(0, largeur_ecran - detail_jeu), 0]
            points += 1  
            vitesse_jeu_d += 0.25 
        
        if collision(mvm_joueur, position_1) or collision(mvm_joueur, position_2):
            game_over = True
            break
        ## Creation de la fenetre
        fenetre(pygame)
    
    display.fill(fond_jeu)
    game_over_tEnemyXt = font.render("Score final : {}".format(points), True, cube_col)
    contiuer = font.render("Appuyez sur 'q' pour quitter", True, finjeu)
    display.blit(game_over_tEnemyXt, (largeur_ecran // 2 - 200, hauteur_ecran // 2 - 60))
    display.blit(contiuer, (largeur_ecran // 2 - 200, hauteur_ecran // 2 - 20))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()