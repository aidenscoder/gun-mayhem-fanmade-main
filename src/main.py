import modules.drawing
from pygame import mouse,key
window = modules.drawing.window(800,600)


def main(window:modules.drawing.window):
    window.draw_rect((400,300,50,50),modules.drawing.ColorRgbA((100,255,0,255)),'Additive')
    window.draw_rect((375,300,50,50),modules.drawing.ColorRgbA((255,0,0,255)),'Additive')
    
window.main_loop = main
