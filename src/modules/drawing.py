import pygame as __game_source__
from typing import Callable,Self,Literal,get_args

number = int|float
__pygame__ = __game_source__


__image_dict__:dict[str,__pygame__.Surface] = {}
def load_img(image,name,width,height):
    base = __pygame__.image.load(image)
    __image_dict__[name] = __pygame__.transform.scale(
        base,(
            width*base.get_width(),
            height*base.get_height()
        )
    )
    __image_dict__[name].convert_alpha()


class ColorRgb(tuple[number,number,number]):
    def __new__(cls,pair = (0,0,0)):
        return super().__new__(cls,pair)

    @property
    def R(self):
        return self[0]
    
    @property
    def G(self):
        return self[1]
    
    @property
    def B(self):
        return self[2]
    
    @property
    def conversion(self) -> tuple[int,...]:
        return tuple(map(lambda x:int(x),self))

    
class ColorRgbA(tuple[number,number,number,number]):    
    def __new__(cls,pair = (0,0,0,255)):
        return super().__new__(cls,pair)

    @property
    def R(self):
        return self[0]
    
    @property
    def G(self):
        return self[1]
    
    @property
    def B(self):
        return self[2]
    
    @property
    def A(self):
        return self[3]
    
    @property
    def conversion(self) -> tuple[int,...]:
        return tuple(map(lambda x:int(x),self))


class window:
    __main_loop__:Callable[[Self],None]
    __main_window__:__pygame__.Surface
    __center__:__pygame__.Surface
    blending_options = Literal['Normal','Additive','Subtractive','Multiplicitive']
    
    def __init__(self,width,height):
        self.__main_window__ = __pygame__.display.set_mode((width,height))
        self.__center__ = __pygame__.Surface((width,height))
    
    @property
    def main_loop(self):
        return self.__main_loop__.__get__(self,type(self))
    
    @main_loop.setter
    def main_loop(self,value) -> None:
        self.__main_loop__ = value
    
    def draw_rect(
        self,
        position,
        color = ColorRgb((0,0,0)),
        draw_type:blending_options = "Normal",
        rotation:number = 0
    ):
        Surface = __pygame__.Surface((position[2],position[3]),__pygame__.SRCALPHA)
        Surface.convert_alpha()
        if isinstance(color,ColorRgb):
            Surface.fill(color.conversion)
        elif isinstance(color,ColorRgbA):
            Surface.fill(color.conversion)
            Surface.set_alpha(color.A)
        Surface = __pygame__.transform.rotate(Surface,rotation)
        center = Surface.get_rect(center=(position[0],position[1]))
        match draw_type:
            case "Normal":
                self.__center__.blit(Surface,center)
            case "Additive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_ADD)
            case "Subtractive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_SUB)
            case "Multiplicitive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_MULT)
            case _:
                raise TypeError(f"Parameter draw_type must be one of the following options:{get_args(self.blending_options)}")
            
    def draw_image(
        self,
        position,
        image:str,
        draw_type:blending_options = "Normal",
        rotation:number = 0
    ):
        Surface = __image_dict__[image]
        Surface.convert_alpha()
        Surface = __pygame__.transform.rotate(Surface,rotation)
        center = Surface.get_rect(center=(position[0],position[1]))
        match draw_type:
            case "Normal":
                self.__center__.blit(Surface,center)
            case "Additive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_ADD)
            case "Subtractive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_SUB)
            case "Multiplicitive":
                self.__center__.blit(Surface,center,special_flags=__pygame__.BLEND_RGBA_MULT)
            case _:
                raise TypeError(f"Parameter draw_type must be one of the following options:{get_args(self.blending_options)}")
    
    def start(self,bg_color:ColorRgb):
        running = True
        while running:
            for event in __pygame__.event.get():
                if event.type == __pygame__.QUIT:
                    running = False
            self.__main_window__.fill(bg_color.conversion)
            self.__center__.fill(bg_color.conversion)
            center = self.__center__.get_rect(center=(self.width/2,self.height/2))
            self.main_loop()
            self.__main_window__.blit(self.__center__,center)
            __pygame__.display.flip()
        __pygame__.quit()
        
    @property
    def width(self) -> int:
        return self.__main_window__.get_width()
    
    @property
    def height(self) -> int:
        return self.__main_window__.get_height()
    
def collide_rect(rect1,rect2):
    surf1 = __pygame__.Surface((rect1[2],rect1[3]))
    surf2 = __pygame__.Surface((rect2[2],rect2[3]))
    surf1.convert_alpha()
    surf2.convert_alpha()
    surf1 = __pygame__.transform.rotate(surf1,rect1[4])
    surf2 = __pygame__.transform.rotate(surf2,rect2[4])
    mask1 = __pygame__.mask.from_surface(surf1)
    mask2 = __pygame__.mask.from_surface(surf2)
    dist1 = surf1.get_rect(center=(rect1[0],rect1[1]))
    dist2 = surf2.get_rect(center=(rect2[0],rect2[1]))
    distance = (dist1.x-dist2.x,dist1.y-dist2.y)
    if mask1.overlap_area(mask2,distance):
        return True
    else:
        return False