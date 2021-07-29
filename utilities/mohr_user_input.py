import pygame
import numpy as np
from utilities.mohr_fonts import game_font
class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,  outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = game_font(15)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + 15 , self.y + int(self.height/5)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    
enterButton = button((180,0,0), 680, 480, 80, 30, 'ENTER')
backButton = button((180,0,0), 30, 10, 80, 30, 'BACK')
generalButton = button((180,0,0), 360, 170, 80, 30, 'GENERAL')
tutorialButton = button((180,0,0), 350, 300, 100, 30, 'TUTORIAL')
quizButton = button((180,0,0), 360, 430, 80, 30, 'QUIZ')
twodButton = button((180,0,0), 360, 170, 80, 30, '2-D')
threedButton = button((180,0,0), 360, 300, 80, 30, '3-D')
startButton = button((180,0,0), 360, 400, 80, 30, 'START')
nextButton = button((180,0,0), 680, 550, 80, 30, 'NEXT')
submitButton = button((180,0,0), 680, 550, 80, 30, 'SUBMIT')
graphButton = button((180,0,0), 530, 550, 80,30, 'GRAPH')
back_to_homeButton = button((180,0,0), 680, 550, 100,30, 'BACK HOME')
stressButton = button((180,0,0), 360, 170, 80, 30, 'STRESS')
strainButton = button((180,0,0), 360, 300, 80, 30, 'STRAIN')
finishButton = button((180,0,0), 680, 550, 80, 30, 'FINISH')

docuButton= button((180,0,0), 50, 550, 140, 30, 'DOCUMENTATION')
aboutButton = button((180,0,0), 680, 550, 80, 30, 'ABOUT')


class inputtextbox():
    def __init__(self, color_inactive, color_active, x,y,width,height):
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = ''
        self.active = True
        self.color = self.color_active if self.active else self.color_inactive

    def render(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)



sigma_xx_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 200, 100, 25)
sigma_yy_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 250, 100, 25)
sigma_zz_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 300, 100, 25)
tau_xy_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 350, 100, 25)
tau_yz_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 400, 100, 25)
tau_zx_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 450, 100, 25)

epsi_xx_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 200, 100, 25)
epsi_yy_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 250, 100, 25)
epsi_zz_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 300, 100, 25)
epsi_xy_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 350, 100, 25)
epsi_yz_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 400, 100, 25)
epsi_zx_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 450, 100, 25)

angle_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 200, 100, 25)
angle1_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 250, 100, 25)
angle2_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 300, 100, 25)
angle3_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 350, 100, 25)

sigma_xx_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 200, 100, 25)
sigma_yy_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 250, 100, 25)
sigma_zz_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 300, 100, 25)
tau_xy_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 350, 100, 25)
tau_yz_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 400, 100, 25)
tau_zx_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 450, 100, 25)

epsi_xx_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 200, 100, 25)
epsi_yy_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 250, 100, 25)
epsi_zz_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 300, 100, 25)
epsi_xy_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 350, 100, 25)
epsi_yz_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 400, 100, 25)
epsi_zx_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 200, 450, 100, 25)

angle_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 200, 100, 25)
angle1_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 250, 100, 25)
angle2_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 300, 100, 25)
angle3_tut = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 550, 350, 100, 25)

C1_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 400, 200, 100, 25)
C2_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 400, 250, 100, 25)
C3_gen = inputtextbox(pygame.Color('lightskyblue3'), pygame.Color('dodgerblue2'), 400, 300, 100, 25)
