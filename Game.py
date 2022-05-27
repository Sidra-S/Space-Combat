import pygame
import random
import math
pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Combat")
icon = pygame.image.load("E:\\clg\\sem2\\Project\\Rocket-Launch-clipart-png-image.png")
pygame.display.set_icon(icon)


# background
bg = pygame.image.load("E:\\clg\\sem2\Project\\space1.v1.cropped.png")

# spaceship
space_ship = pygame.image.load("E:\\clg\\sem2\\Project\\ss.png")
space_ship = pygame.transform.scale(space_ship, (90, 100))
SP_X = 360
SP_Y = 480
s_ship_variable_pos = 0


def display_ship(x, y):
    window.blit(space_ship, (x, y))


#hijacked spaceship
hij_ss = (pygame.image.load("E:\\clg\\sem2\\Project\\Final HS.png"))
hij_ss = pygame.transform.scale(hij_ss, (130,105))
hij_ss_X = (random.randint(0, 800))
hij_ss_Y = (random.randint(50, 150))
hij_ss_variable_pos_x = 2
hij_ss_variable_pos_y = 2

def display_hij_ss(x, y):
    window.blit(hij_ss, (x, y))

# enemy
enemy = []
E_X = []
E_Y = []
enemy_variable_pos_x = []
enemy_variable_pos_y = []
no_enemy = 6
for i in range(no_enemy):
    enemy.append(pygame.image.load("E:\\clg\\sem2\Project\\Enemy.png"))
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

#hij_ss collision
def collision_hij(hij_ss_X,hij_ss_Y,B_X,B_Y):
    dist=math.sqrt(math.pow(hij_ss_X-B_X,2)+math.pow(hij_ss_Y-B_Y,2))
    if dist < 35:
        return True
    else:
        return False

#scoring sys
score=0
font = pygame.font.Font('freesansbold.ttf',32)
X = 10
Y = 10

over = pygame.font.Font('freesansbold.ttf',75)

def display_score(X,Y):
    s = font.render("Score : "+ str(score),True, (139,0,139))
    window.blit(s, (X,Y))

clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

def game_over():
    for i in range(80):
        g = over.render("GAME OVER!!! ", True, (128, 0, 0))
        window.blit(g, (150, 250))


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

    # spaceship logic
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

    #hijack logic
    hij_ss_X += hij_ss_variable_pos_x
    if hij_ss_X <= 0:
        hij_ss_X = 736
    if hij_ss_X >= 736:
        hij_ss_X = 5
    display_hij_ss(hij_ss_X,hij_ss_Y)
    if collision_hij(hij_ss_X, hij_ss_Y, B_X, B_Y):
        B_Y = 480
        score -= 3
        print(score)
        b_state = False

        hij_ss_X = random.randint(0, 765)
        hij_ss_Y = random.randint(50, 150)

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
    if (frame_count >= 5450) and (frame_count <= 5520):
        game_over()

    if frame_count == 5520:
        pygame.quit()

    display_score(X,Y)
    pygame.display.update()


pygame.quit()


