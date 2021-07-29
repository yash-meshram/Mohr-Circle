import pygame
# import MohrCircle_new
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_screen import *
# from mohr_window_list import windows

def incompatible_input_window(screen, prev_win, windows):
    backButton.draw(screen, (0,0,0))
    Big_font = game_font(55)
    Small_font = game_font(20)
    text = Big_font.render("Incompatible input!!!!", 1, (0,0,0))
    screen.blit(text, (70, 250))
    text = Small_font.render ("Please fill all the fields", 1,(0,0,0))
    screen.blit(text, (200, 400))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                
                windows[prev_win][1].makeCurrent()
                incompatible_input_window_check.endCurrent()
            
        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)
