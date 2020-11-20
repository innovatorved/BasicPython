import pygame
import random
from time import sleep
import math

score = 0
# initalize pygame
pygame.init()

# define game window size
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption('Airo_Zone')  # title

icon = pygame.image.load('paper-plane.png')  # icon load from gallery
pygame.display.set_icon(icon)  # icon succesfully added

# background
bg = pygame.image.load('Space.jpg')

# blast
blast = pygame.image.load('fire.png')

# bullet
# Ready _ you can't see the bullet
# Fire - the bullet is fire
but_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 3
bullet_state = 'ready'

pygame.display.update()  # Use for display Update

# Player
play_img = pygame.image.load('game_pro.png')
playerX = 370
playerY = 500
playerX_change = 0

# enemy

emy_img = pygame.image.load('enemy.png')
enemyX = random.randint(20, 770)
enemyY = random.randint(50, 150)
enemyX_change = 2
enemyY_change = 40


def player(x, y):
    screen.blit(play_img, (x, y))  # drawing an player image


def blast_space(x, y):
    screen.blit(blast, (x, y))


def enemy(x, y):
    screen.blit(emy_img, (x, y))  # drawing an enemy image


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(but_img, (x + 16, y + 10))


def coll(enemyX, enemyY, bulletX, bulletY):
    distance = (((bulletX - enemyX) ** 2) + ((bulletY - enemyY) ** 2)) // 2
    if distance < 200:
        blast_space(enemyX, enemyY)
        return True
    else:
        return False


# Game loop
running = True

while running:
    # for closing window
    # background Color
    # RGB - Red , Green ,Blue
    screen.fill((215, 200, 120))
    # BG image
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 3

            if event.key == pygame.K_RIGHT:
                playerX_change += 3

            if event.key == pygame.K_SPACE:
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        if event.type == pygame.QUIT:
            running = False
            screen = pygame.quit()

    # checking the boundaries for enemy and player

    # Enemy Movement
    enemyX += enemyX_change

    if enemyX <= 15:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 720:
        enemyX_change = -2
        enemyY += enemyY_change

    if enemyY >= 520:  # returning enemy to top
        enemyY = 50

    # player movement control
    if playerX >= 720:
        playerX_change = 0
        playerX = 715
    elif playerX <= 15:
        playerX_change = 0
        playerX = 20
    else:
        playerX += playerX_change

    # Bullet Movement
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if bulletY <= 10:
        bulletY = 500
        bullet_state = 'ready'

    # collistion
    data = coll(enemyX, enemyY, bulletX, bulletY)
    if data == True:
        blast_space(enemyX, enemyY)
        bulletY = 500
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(20, 770)
        enemyY = random.randint(50, 150)
        player(playerX, playerY)
        pygame.display.update()
        sleep(0.5)


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    blast_space(800, 600)
    pygame.display.update()
