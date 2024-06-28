import pygame
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((900,600),pygame.RESIZABLE)
window.fill((255,255,255))
title=pygame.display.set_caption("YRR")
Icon=pygame.image.load("suiiiiii.jpg")
pygame.display.set_icon(Icon)

circ_position=[]
radius=60
col=(255,255,0)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==MOUSEBUTTONDOWN:
            position=event.pos
            circ_position.append(position)
    for position in circ_position:
        pygame.draw.circle(window,col,position,radius)
    pygame.display.update()
