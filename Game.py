import pygame
import random
import math
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
enemy = []
E_X = []
E_Y = []
enemy_variable_pos_x = []
enemy_variable_pos_y = []
no_enemy = 7
for i in range(no_enemy):
    enemy.append(pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\Enemy.png"))
    E_X.append(random.randint(0, 800))
    E_Y.append(random.randint(50, 150))
    enemy_variable_pos_x.append(3)
    enemy_variable_pos_y.append(3)


def display_enemy(x, y, i):
    window.blit(enemy[i], (x, y))


# bullet
bullet = pygame.image.load("D:\\Sidra\\Decision Modeling\\Project\\b2.png")
bullet = pygame.transform.scale(bullet, (60, 50))
B_X = 0
B_Y = 460
b_variable_pos_y = 17

b_state = False


def fire_bullets(x, y):
    window.blit(bullet, (x, y))
#collision
def collision_detection(E_X,E_Y,B_X,B_Y):
    dist=math.sqrt(math.pow(E_X-B_X,2)+math.pow(E_Y-B_Y,2))
    if dist <20:
        return True
    else:
        return False
#scorring sys
score=0
font = pygame.font.Font('freesansbold.ttf',32)
X = 10
Y = 10

def display_score(X,Y):
    s = font.render("Score : "+ str(score),True, (139,0,139))
    window.blit(s , (X,Y))

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

    if B_Y<=0:
        B_Y=480
        b_state=False


    # enemy logic
    for i in range(no_enemy):
        E_X[i] += enemy_variable_pos_x[i]
        if collision_detection(E_X[i],E_Y[i],B_X,B_Y):
            B_Y=480
            score+=5
            print(score)
            b_state=False

            E_X[i]=random.randint(0,735)
            E_Y[i]=random.randint(50, 150)


        #if E_X[i] <= 0:
            #enemy_variable_pos_x[i] = 4
            #E_Y[i] += enemy_variable_pos_y[i]
        #if E_X[i] > 736:
            #enemy_variable_pos_x[i] = -4
            #E_Y[i] += enemy_variable_pos_y[i]

        display_enemy(E_X[i], E_Y[i], i)
    display_score(X,Y)
    pygame.display.update()

pygame.quit()


