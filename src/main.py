from modules import drawing
from modules.keybinds import *
window = drawing.window(800,600)

drawing.load_img(r'src\assets\bg layer 1.png','bg-1',1.5,1.5)
drawing.load_img(r'src\assets\bg layer 2.png','bg-2',1.5,1.5)
camera_x:drawing.number = 0
camera_y:drawing.number = 0

class rect:
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
    
    @property
    def conversion_NonRotation(self):
        return (self.x,self.y,self.size_x,self.size_y)
    
    def conversion_offset(self,x:drawing.number,y:drawing.number):
        return (self.x-x,self.y-y,self.size_x,self.size_y,self.rotation)
    
    def conversion_offset_NonRotation(self,x:drawing.number,y:drawing.number):
        return (self.x-x,self.y-y,self.size_x,self.size_y)


collisions = [rect(400,500,100,50,0)]
my_rect = rect(400,300,50,50,0)

def main(window:drawing.window,speed=[0,0]):
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
                to_return.append(drawing.collide_rect(i.conversion,compare_rect))
                window.draw_rect(
                    i.conversion_offset_NonRotation(camera_x,camera_y),
                    rotation=i.rotation
                )
            return to_return
            
    camera_x = Mouse.x - window.width/2
    camera_y = Mouse.y - window.height/2
    window.draw_image((400-camera_x*0.05,500-camera_y*0.05),'bg-2')
    window.draw_image((400-camera_x*0.1,500-camera_y*0.1),'bg-1')
    
    current = get_colliding(my_rect.conversion)
    
    if Keyboard.is_pressed(Key.key_a,Key.key_LEFT):
        speed[0] -= 5
    if Keyboard.is_pressed(Key.key_d,Key.key_RIGHT):
        speed[0] += 5
    if Keyboard.is_pressed(Key.key_w,Key.key_UP):
        speed[1] -= 5
    if Keyboard.is_pressed(Key.key_s,Key.key_DOWN):
        speed[1] += 5
        
    speed[0] *= 0.8
    speed[1] *= 0.8
    my_rect.x += speed[0]
    my_rect.y += speed[1]
    
        
    window.draw_rect(
        my_rect.conversion_offset_NonRotation(camera_x,camera_y),
        drawing.ColorRgbA((255,0,0,255))
    )
    
window.main_loop = main
window.start(bg_color=drawing.ColorRgb((100,175,255)))