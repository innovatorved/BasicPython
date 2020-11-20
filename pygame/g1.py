import pygame

#Intialize the pygame
pygame.init()

#creating Screen
screen = pygame.display.set_mode((800,600))

runing = True
while runing:
    for event in pygame.event.get(): #all we pressend in pygame window all is event accept close button
        if event.type == pygame.QUIT():
            runing = False
        
