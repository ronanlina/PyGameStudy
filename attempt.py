#!/usr/bin/python

import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720)) #screen size (?)
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert() #converts surface to single pixel format
    background.fill((250, 250, 250)) #background color

    # Display some text
    font = pygame.font.Font(None, 36) #text font setting
    text = font.render("Hello There", 1, (10, 10, 10))#creating text object. text, AA or not, color grain
    textpos = text.get_rect() #setting text rectangle
    textpos.centerx = background.get_rect().centerx #setting to be equals with background's centerx (center position)
    background.blit(text, textpos) # renders background

    # Blit everything to the screen . rendering
    screen.blit(background, (0, 0))
    pygame.display.flip() # flip = update

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_1:
                    pygame.draw.circle(screen, (0,0,0), (200,200), 5)
                    pygame.display.flip()

        # screen.blit(background, (0, 0))
        # pygame.display.flip()

def drawCircle():
    pos=getPos()
    pygame.draw.circle(screen, (  0,   0, 255), pos, 20) 

if __name__ == '__main__': main()