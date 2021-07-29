import pygame
# import MohrCircle_stress
import window_types.pop_up as pop_up
import time
import random
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_screen import *
import os

iitgn_logo = pygame.image.load("Images/iitgn.png")
iitgn_logo = pygame.transform.scale(iitgn_logo, (250, 250))

def startwindow(screen, prev_win, windows):
    Big_font = game_font(80)
    Small_font = game_font(20)
    text = Big_font.render("Mohr's Circle", 1, (0,0,0))
    screen.blit(text, (70, 250))
    screen.blit(iitgn_logo, (280,0))
    new_text =["An interactive app to understand and visualise the concepts",
                "   of Mohr's Circle in 2-Dimeansion and 3-Dimension"]
    count = 0
    for text_inp in new_text:
        text = Small_font.render(text_inp,1,(0,0,0))
        screen.blit(text,(60, 400+count))
        count+=25
    # text = Small_font.render ("An interactive app to understand and visualise the concepts of Mohr's Circle in 2-Dimeansion and 3-Dimension",1, (0,0,0))
    # screen.blit(text, (60, 400))
    text = Small_font.render ("Rwik Rana| Shreyas Sonawane| Manish Alriya| Yash Meshram ",1, (0,0,0))
    screen.blit(text, (60, 550))
    enterButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if enterButton.isOver(pos):
                enterWindow_check.makeCurrent()
                startwindow_check.endCurrent()
                print("User entered the Application")
        if event.type == pygame.MOUSEMOTION:
            if enterButton.isOver(pos):
                enterButton.color = (255, 0, 0)
            else:
                enterButton.color = (180, 0, 0)

def enterwindow(screen, prev_win, windows):
    Small_font = game_font(20)
    text = Small_font.render ("Select Mode",1, (0,0,0))
    screen.blit(text, (360, 100))

    generalButton.draw(screen, (0,0,0))
    tutorialButton.draw(screen, (0,0,0))
    quizButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))
    docuButton.draw(screen, (0,0,0))
    aboutButton.draw(screen,(0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if generalButton.isOver(pos):
                gen_stress_strain_window_check.makeCurrent()
                enterWindow_check.endCurrent()
                print("Entering in General Mode")
            if quizButton.isOver(pos):
                quizwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
                print("Entering in Quiz Mode")
            if tutorialButton.isOver(pos):
                tutorialwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
            if backButton.isOver(pos):
                startwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
            if aboutButton.isOver(pos):
                aboutwindow_check.makeCurrent()
                enterWindow_check.endCurrent()
            if docuButton.isOver(pos):
                try:
                    os.system('Mohr_Circle_Documentation.pdf')
                except:
                    pass
        if event.type == pygame.MOUSEMOTION:
            if generalButton.isOver(pos):
                generalButton.color = (255, 0, 0)
            else:
                generalButton.color = (180, 0, 0) 
            if tutorialButton.isOver(pos):
                tutorialButton.color = (255, 0, 0)
            else:
                tutorialButton.color = (180, 0, 0) 
            if quizButton.isOver(pos):
                quizButton.color = (255, 0, 0)
            else:
                quizButton.color = (180, 0, 0) 
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)
            if docuButton.isOver(pos):
                docuButton.color = (255, 0, 0)
            else:
                docuButton.color = (180, 0, 0)

def aboutwindow(screen, prev_win, windows):
    Small_font = game_font(20)
    Big_font = game_font(40)
    text = Big_font.render ("ABOUT US",1, (0,0,0))
    screen.blit(text, (330, 100))
    texts = ["We are a group of 4 students from IITGn.",
            "This is a term project for the course ",
            "ME-321 Mechanics of Deformable Bodies.",
            "The app is targeted towards students", 
            "encountering the topicsof Stress, Strain",
            "Mohr's Circle. This app helps user to learn,",
            "to draw Mohr Circle and evaluate his/her",
            "learnings using Quiz mode."]
    count = 0
    for text in texts:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(150, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                aboutwindow_check.endCurrent()

        if event.type == pygame.MOUSEMOTION:

            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

