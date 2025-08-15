from modules import drawing
from modules.keybinds import *
window = drawing.window(800,600)

drawing.load_img(r'src\assets\bg layer 1.png','bg-1',1.5,1.5)
drawing.load_img(r'src\assets\bg layer 2.png','bg-2',1.5,1.5)
camera_x:drawing.number = 0
camera_y:drawing.number = 0

class positioner:
    def __init__(self,
        x:drawing.number,
        y:drawing.number,
        size_x:drawing.number,
        size_y:drawing.number,
        rotation:drawing.number
    ) -> None:
        self.x:drawing.number = x
        self.y:drawing.number = y
        self.size_x:drawing.number = size_x
        self.size_y:drawing.number = size_y
        self.rotation:drawing.number = rotation
        
    @property
    def conversion(self):
        return (self.x,self.y,self.size_x,self.size_y,self.rotation)

collisions = [(400,500,100,25)]
def main(window:drawing.window):
    global camera_x,camera_y 
    Mouse.update()
    def get_colliding(
        compare_rect:tuple[
            drawing.number,
            drawing.number,
            drawing.number,
            drawing.number,
            drawing.number
            ]
        ):
            to_return = []
            for i in collisions:
                to_return.append(drawing.collide_rect((*i,0),compare_rect))
            return to_return
            
    
    camera_x = Mouse.x - window.width/2
    camera_y = Mouse.y - window.height/2
    #window.draw_image((400-camera_x*0.05,500-camera_y*0.05),'bg-2')
    #window.draw_image((400-camera_x*0.1,500-camera_y*0.1),'bg-1')
    print(get_colliding(positioner(400,300,50,50,0).conversion))
    window.draw_rect((400,300,50,50),drawing.ColorRgbA((255,0,0,150)),"Additive")
    
window.main_loop = main
window.start(bg_color=drawing.ColorRgb((100,175,255)))