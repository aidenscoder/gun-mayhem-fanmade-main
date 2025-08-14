import pygame
from typing import Callable,Self,Literal,get_args

number = int|float

__image_dict__:dict[str,pygame.Surface]
def load_img(image,width,height):
    __image_dict__[image] = pygame.transform.scale(pygame.image.load(image),(width,height))
    __image_dict__[image].convert_alpha()


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
    __main_window__:pygame.Surface
    __center__:pygame.Surface
    blending_options = Literal['Normal','Additive','Subtractive','Multiplicitive']
    
    def __init__(self,width,height):
        self.__main_window__ = pygame.display.set_mode((width,height))
        self.__center__ = pygame.Surface((width,height))
    
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
        Surface = pygame.Surface((position[2],position[3]),pygame.SRCALPHA)
        Surface.convert_alpha()
        Surface.fill(color.conversion)
        Surface = pygame.transform.rotate(Surface,rotation)
        center = Surface.get_rect(center=(position[0],position[1]))
        match draw_type:
            case "Normal":
                self.__center__.blit(Surface,center)
            case "Additive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_ADD)
            case "Subtractive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_SUB)
            case "Multiplicitive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_MULT)
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
        Surface = pygame.transform.rotate(Surface,rotation)
        center = Surface.get_rect(center=(position[0],position[1]))
        match draw_type:
            case "Normal":
                self.__center__.blit(Surface,center)
            case "Additive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_ADD)
            case "Subtractive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_SUB)
            case "Multiplicitive":
                self.__center__.blit(Surface,center,special_flags=pygame.BLEND_RGBA_MULT)
            case _:
                raise TypeError(f"Parameter draw_type must be one of the following options:{get_args(self.blending_options)}")
    
    def start(self,bg_color:ColorRgb):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.__main_window__.fill(bg_color.conversion)
            self.__center__.fill(bg_color.conversion)
            center = self.__center__.get_rect(center=(self.width/2,self.height/2))
            self.main_loop()
            self.__main_window__.blit(self.__center__,center)
            pygame.display.flip()
        pygame.quit()
        
    @property
    def width(self) -> int:
        return self.__main_window__.get_width()
    
    @property
    def height(self) -> int:
        return self.__main_window__.get_height()