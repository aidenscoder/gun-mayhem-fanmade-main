import modules.drawing as drawing
window = drawing.window(800,600)

def main(window:drawing.window):
    window.draw_rect((400,300,50,50),drawing.ColorRgbA((100,255,0,255)),'Additive')
    window.draw_rect((375,300,50,50),drawing.ColorRgbA((255,0,0,255)),'Additive')
    
window.main_loop = main
