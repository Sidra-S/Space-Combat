import pygame
import random

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Combat")
icon = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\Rocket-Launch-clipart-png-image.png")
pygame.display.set_icon(icon)

# background
bg = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\space1.v1.cropped.png")

# spaceship
space_ship = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\Spaceship.png")
space_ship = pygame.transform.scale(space_ship, (90, 100))
SP_X = 360
SP_Y = 480
s_ship_variable_pos = 0


def display_ship(x, y):
    window.blit(space_ship, (x, y))


# enemy
enemy = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\Enemy.png")
enemy = pygame.transform.scale(enemy, (60, 70))
E_X = random.randint(0, 800)
E_Y = random.randint(50, 150)
enemy_variable_pos_x = 3
enemy_variable_pos_y = 3


def display_enemy(x, y):
    window.blit(enemy, (x, y))


# bullet
bullet = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\b2.png")
bullet = pygame.transform.scale(bullet, (60, 50))
B_X = 0
B_Y = 460
b_variable_pos_y = 8

b_state = False


def fire_bullets(x, y):
    window.blit(bullet, (x, y))


run = True
while run:

    window.blit(bg, (0, 0))
    # window.fill((255,0,45))
    # event loop
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                s_ship_variable_pos += 2
            if e.key == pygame.K_LEFT:
                s_ship_variable_pos -= 2

            if e.key == pygame.K_SPACE and b_state == False:
                B_X = SP_X
                b_state = True

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
                s_ship_variable_pos = 0
    # logic
    SP_X += s_ship_variable_pos
    if SP_X <= 0:
        SP_X = 0
    if SP_X > 720:
        SP_X = 720
    display_ship(SP_X, SP_Y)

    # bullet logic
    if b_state:
        B_Y -= b_variable_pos_y
        fire_bullets(B_X + 15, B_Y + 15)

    # enemy logic
    E_X += enemy_variable_pos_x
    if E_X <= 0:
        enemy_variable_pos_x = 3
        E_Y += enemy_variable_pos_y
    if E_X > 736:
        enemy_variable_pos_x = -3
        E_Y += enemy_variable_pos_y

    display_enemy(E_X, E_Y)

    pygame.display.update()

pygame.quit()


