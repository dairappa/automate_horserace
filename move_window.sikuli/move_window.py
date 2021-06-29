# -*- coding: utf-8 -*-
from sikuli import *

def resizeUmamusume():
    switchApp("umamusume")
    sleep(1)
    title = find(Pattern("1620895568437.png").targetOffset(-22,-1))
    drop_point = title.getTarget().offset(-title.getX() + 8, -title.getY() + 7)
    dragDrop(title, drop_point)
    sleep(1)
    
    title = find(Pattern("1620895568437.png").targetOffset(-22,-1))
    corner = find(Pattern("1620896396237.png").targetOffset(91,-3))

    current_width = corner.getX() - title.getX()
    delta = 465 - current_width
    
    drop_point = corner.getTarget().offset(delta, 0)
    dragDrop(corner, drop_point)
    sleep(1)

resizeUmamusume()

