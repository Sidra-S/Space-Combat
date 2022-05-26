import pygame
import random
import math
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Combat")
icon = pygame.image.load("E:\\clg\\sem2\\Project\\Rocket-Launch-clipart-png-image.png")
pygame.display.set_icon(icon)


# background
bg = pygame.image.load("E:\\clg\\sem2\\Project\\space1.v1.cropped.png")

# spaceship
space_ship = pygame.image.load("E:\\clg\\sem2\\Project\\ss.png")
space_ship = pygame.transform.scale(space_ship, (90, 100))
SP_X = 360
SP_Y = 480
s_ship_variable_pos = 0


def display_ship(x, y):
    window.blit(space_ship, (x, y))


#hijacked spaceship
#hij_ss = (pygame.image.load("E:\\clg\\sem2\\Project\\hij_ss.png"))
#hij_ss_X = (random.randint(0, 800))
#hij_ss_Y = (random.randint(50, 150))
#hij_ss_variable_pos_x = 20
#hij_ss_variable_pos_y = 20
#no_hij_ss = 2

#def display_hij_ss(x, y, i):
    #window.blit(hij_ss[i], (x, y))

# enemy
enemy = []
E_X = []
E_Y = []
enemy_variable_pos_x = []
enemy_variable_pos_y = []
no_enemy = 7
for i in range(no_enemy):
    enemy.append(pygame.image.load("E:\\clg\\sem2\\Project\\Enemy.png"))
    E_X.append(random.randint(0, 800))
    E_Y.append(random.randint(50, 150))
    enemy_variable_pos_x.append(4)
    enemy_variable_pos_y.append(4)


def display_enemy(x, y, i):
    window.blit(enemy[i], (x, y))


# bullet
bullet = pygame.image.load("E:\\clg\\sem2\\Project\\b2.png")
bullet = pygame.transform.scale(bullet, (60, 50))
B_X = 0
B_Y = 460
b_variable_pos_y = 10

b_state = False


def fire_bullets(x, y):
    window.blit(bullet, (x, y))
#collision
def collision_detection(E_X,E_Y,B_X,B_Y):
    dist=math.sqrt(math.pow(E_X-B_X,2)+math.pow(E_Y-B_Y,2))
    if dist < 35:
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

clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
frame_rate = 60
start_time = 90
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
                s_ship_variable_pos += 15
             if e.key == pygame.K_LEFT:
                s_ship_variable_pos -= 15

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


        if E_X[i] <= 0:
            enemy_variable_pos_x[i] = 4
            E_Y[i] += enemy_variable_pos_y[i]
        if E_X[i] > 736:
            enemy_variable_pos_x[i] = -4
            E_Y[i] += enemy_variable_pos_y[i]

        display_enemy(E_X[i], E_Y[i], i)

        # Calculate total seconds
    total_seconds = frame_count // frame_rate

        # Divide by 60 to get total minutes
    minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
    text = font.render(output_string, True, (139,0,139))
    window.blit(text, [650, 10])

        # --- Timer going down ---
        # --- Timer going up ---
        # Calculate total seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

        # Divide by 60 to get total minutes
    minutes = total_seconds // 60

        # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60

        # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

        # Blit to the screen
    text = font.render(output_string, True, (139,0,139))

    window.blit(text, [650, 25])

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

        # Limit frames per second
    clock.tick(frame_rate)
    if frame_count == 5500:
        GAME_FONT = pygame.freetype.Font("freesansbold.ttf", 50)
        GAME_FONT.render_to(window, (400, 350), "Game Over!", (139, 0, 139))

    if frame_count == 5600:
        pygame.quit()

    display_score(X,Y)
    pygame.display.update()


pygame.quit()


