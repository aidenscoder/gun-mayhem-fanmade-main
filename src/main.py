import drawing,random
from typing import Any
window = drawing.window(800,600)

pair:tuple[drawing.number,drawing.number,drawing.number]|Any = [255,255,0]
def main(window:drawing.window):
    global pair
    pair = list(map(lambda x:min(max(x,0),255),pair))
    repeat = lambda times,item: [item for _ in range(times)]
    pair[0] = random.uniform(0,255)
    pair[1] = random.uniform(0,255)
    pair[2] = random.uniform(0,255)
    window.draw_rect((400,300,50,50),drawing.ColorRgb((pair[0],pair[1],pair[2])),draw_type="Additive")
    
window.main_loop = main

window.start(drawing.ColorRgb((255,255,0)))