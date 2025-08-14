from modules import drawing
from modules.keybinds import *
import pygame
window = drawing.window(800,600)


def main(window:drawing.window):
    window.draw_rect((125,300,200,50))
    window.draw_rect((625,300,200,50))
    window.draw_rect((400,500,500,50))
window.main_loop = main
window.start(bg_color=drawing.ColorRgb((255,255,255)))