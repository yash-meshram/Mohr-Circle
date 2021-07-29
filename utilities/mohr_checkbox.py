import pygame
import numpy as np
from utilities.mohr_fonts import game_font
class checkBox():
    def __init__(self, color_inactive, color_active, x,y,width,height):
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = False
        self.color = self.color_active if self.active else self.color_inactive
    def draw_circ(self):
        return (0,200,100),(self.x+10,self.y+10), 7
    def render(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
check1 = checkBox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 30, 250, 20, 20)
check2 = checkBox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 30, 300, 20, 20)
check3 = checkBox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 30, 350, 20, 20)
check4 = checkBox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 30, 400, 20, 20)
