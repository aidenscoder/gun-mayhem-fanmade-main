import pygame
from typing import Callable,Self,Literal

number = int|float

__image_dict__:dict[str,pygame.Surface]
def load_img(image:str,width:float,height:float):...

class ColorRgb(tuple[number,number,number]):
    def __new__(cls,pair:tuple[number,number,number] = (0,0,0)) -> Self: ...

    @property
    def R(self) -> number:...   
    
    @property
    def G(self) -> number:... 
    
    @property
    def B(self) -> number:... 
    
    @property
    def conversion(self) -> tuple[number,number,number]:...
    
class ColorRgbA(tuple[number,number,number,number]):    
    def __new__(cls,pair:tuple[number,number,number,number] = (0,0,0,255)) -> Self: ...

    @property
    def R(self) -> number:...   
    
    @property
    def G(self) -> number:... 
    
    @property
    def B(self) -> number:... 
    
    @property
    def A(self) -> number:...

    @property
    def conversion(self) -> tuple[number,number,number]:...

class window:
    __main_loop__:Callable[[Self],None]
    __main_window__:pygame.Surface
    __center__:pygame.Surface
    
    def __init__(self,width:int,height:int) -> None:...
    
    @property
    def main_loop(self) -> Callable[[Self],None]:...
    
    @main_loop.setter
    def main_loop(self,value:Callable[[Self],None]) -> None:...
    
    blending_options = Literal['Normal','Additive','Subtractive','Multiplicitive']
    def draw_rect(
        self,
        position:tuple[number,number,number,number],
        color:ColorRgb|ColorRgbA = ColorRgb((0,0,0)),
        draw_type:blending_options = "Normal",
        rotation:number = 0
    ) -> None:...
    
    def draw_image(
        self,
        position:tuple[number,number],
        color:ColorRgb|ColorRgbA = ColorRgb((0,0,0)),
        draw_type:blending_options = "Normal",
        rotation:number = 0
    ) -> None:...
    
    def start(self,bg_color:ColorRgb) -> None:...
    
    @property
    def width(self) -> int:...
    
    @property
    def height(self) -> int:...
