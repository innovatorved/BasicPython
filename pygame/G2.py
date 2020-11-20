import pygame

#initalize pygame
pygame.init()

#define game window size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption('Airo_Zone')  #title

icon = pygame.image.load('D:\\Icon\\paper-plane.png')#icon load from gallery
pygame.display.set_icon(icon) #icon succesfully added

pygame.display.update()   #Use for display Update

#Player
play_img = pygame.image.load('D:\\Icon\\air_play.png')
playerX = 370
playerY = 500
player_change = 0


def player(x,y):
    screen.blit(play_img,(x,y)) #drawing an image



#Game loop
running = True
while running:  #for closing window
    #background Color
    #RGB - Red , Green ,Blue
    screen.fill((255,200,120))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print('c')
            
            if event.key== pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('ryt')
        if event.type == pygame.QUIT:
            running = False
            screen = pygame.quit()
            print('b')

        

        if event.type == pygame.KEYUP:
            print('d')
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print('release')
                
    player(playerX,playerY)
    pygame.display.update()

