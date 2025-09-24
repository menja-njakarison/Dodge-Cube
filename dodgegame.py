## Importation des librairies necessaires
import pygame
import random

## Initialisation de pygame
pygame.init()

display_width = 880
display_height = 600
color1 = (51,204,204)
color2 = (0,0,0)
color3 = (255, 0, 0)
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dodger Game Using Pygame")
frame_rate = pygame.time.Clock()
gamer_detail = 45
gamer_movement = [display_width // 2, display_height - 2 * gamer_detail]

gamer_speed = 15
to_dodge_detail = 45
to_dodge_position1 = [random.randint(0, display_width - to_dodge_detail), 0]
to_dodge_position2 = [random.randint(0, display_width - to_dodge_detail), 0]
to_dodge_speed = 10
points = 0
font = pygame.font.SysFont("calibri", 35)

def check_for_colision(gamer_movement, enemy_pos):
    p_x, p_y = gamer_movement
    e_x, e_y = enemy_pos
    if (e_x < p_x < e_x + to_dodge_detail or e_x < p_x + gamer_detail < e_x + to_dodge_detail) and \
            (e_y < p_y < e_y + to_dodge_detail or e_y < p_y + gamer_detail < e_y + to_dodge_detail):
        return True
    return False

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        gamer_movement[0] -= gamer_speed
    if keys[pygame.K_RIGHT]:
        gamer_movement[0] += gamer_speed
    if gamer_movement[0] < 0:
        gamer_movement[0] = 0
    elif gamer_movement[0] > display_width - gamer_detail:
        gamer_movement[0] = display_width - gamer_detail
    display.fill(color2)
    to_dodge_position1[1] += to_dodge_speed
    to_dodge_position2[1] += to_dodge_speed
    if to_dodge_position1[1] > display_height:
        to_dodge_position1 = [random.randint(0, display_width - to_dodge_detail), 0]
        points += 1  
        to_dodge_speed += 0.5 
    if to_dodge_position2[1] > display_height:
        to_dodge_position2 = [random.randint(0, display_width - to_dodge_detail), 0]
        points += 1  
        to_dodge_speed += 0.5 
    if check_for_colision(gamer_movement, to_dodge_position1) or check_for_colision(gamer_movement,
                                                                                   to_dodge_position2):
        game_over = True
        break
    pygame.draw.rect(display, color3, (to_dodge_position1[0], to_dodge_position1[1],
                                       to_dodge_detail, to_dodge_detail))
    pygame.draw.rect(display, color3, (to_dodge_position2[0], to_dodge_position2[1], 
                                       to_dodge_detail, to_dodge_detail))
    pygame.draw.rect(display, color1, (gamer_movement[0], gamer_movement[1],
                                       gamer_detail, gamer_detail))
    score_text = font.render("Score: {}".format(points), True, color1)
    display.blit(score_text, (10, 10))
    pygame.display.update()
    frame_rate.tick(30)

display.fill(color2)
game_over_text = font.render("Final Score: {}".format(points), True, color1)
display.blit(game_over_text, (display_width // 2 - 200, display_height // 2 - 20))
pygame.display.update()
pygame.time.wait(3000)
pygame.quit()