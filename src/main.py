from modules import drawing
from modules.keybinds import *
window = drawing.window(800,600)

drawing.load_img(r'src\assets\bg layer 1.png','bg-1',1.5,1.5)
drawing.load_img(r'src\assets\bg layer 2.png','bg-2',1.5,1.5)
camera_x:drawing.number = 0
camera_y:drawing.number = 0

def main(window:drawing.window):
    global camera_x,camera_y 
    Mouse.update()
    
    camera_x = Mouse.x - window.width/2
    camera_y = Mouse.y - window.height/2
    #window.draw_image((400-camera_x*0.05,500-camera_y*0.05),'bg-2',"Additive")
    #window.draw_image((400-camera_x*0.1,500-camera_y*0.1),'bg-1',"Additive")
    window.draw_rect((425,300,50,50),drawing.ColorRgbA((255,0,0,100)),"Additive")
    window.draw_rect((450,300,50,50),drawing.ColorRgbA((0,255,0,100)),"Additive")
window.main_loop = main
window.start(bg_color=drawing.ColorRgb((0,0,0)))