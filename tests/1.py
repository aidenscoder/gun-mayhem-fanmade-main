import pygame
from time import sleep

screen = pygame.display.set_mode((800,600))
overlay = pygame.Surface((100, 100), pygame.SRCALPHA)
screen.fill((0,0,0))
overlay.fill((255, 0, 0, 0))  # Semi-transparent red
screen.blit(overlay, (0, 0),special_flags=pygame.BLEND_RGBA_ADD) 
pygame.display.flip()
sleep(1)
pygame.quit()