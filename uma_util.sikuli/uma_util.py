# -*- coding: utf-8 -*-
from sikuli import *

reg = Region(0,0,601,1111)

def waitClick(image, waitSecond = 15):
    reg.wait(image, waitSecond)
    reg.click()

