import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
import random
from utilities.mohr_screen import *
from MohrCircle_stress import Stress_MohrCircle
from MohrCircle_stress_tut import tut_Stress_MohrCircle

angle_check = 0
sigma1, sigma2, curr_angle = None,None,None
def tutorialwindow(screen, prev_win, windows):
    Small_font = game_font(40)
    extra_small_font = game_font(18)
    text = Small_font.render("Tutorial Mode",1, (0,0,0))
    screen.blit(text, (220, 100))

    twodButton.draw(screen, (0,0,0))
    threedButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))
    note_text = ["NOTE: This is a step-by-step tutorial to",
                 "draw Mohr Circle for Stresses in 2-D and",
                 "3-D only. The entire procedure for strains",
                 "both in 2-D and 3-D are similar, the user",
                 "has to plot (1/2)*(shear values) in 2-D",
                 "and place half of the (1/2)*(shear values)",
                 "in stress tensor for 3-D strain Mohr-Circle."]
    count =0
    for text in note_text:
        text = extra_small_font.render(text,1,(0,0,0))
        screen.blit(text,(180, 380+count))
        count+=30
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if twodButton.isOver(pos):
                    tut2D_stress_input_window_check.makeCurrent()
                    tutorialwindow_check.endCurrent()
                    print("Entering in stress 2-D Mode")
            if threedButton.isOver(pos):
                    tut3D_stress_input_window_check.makeCurrent()
                    tutorialwindow_check.endCurrent()
                    print("Entering in 3-D Mode")
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                tutorialwindow_check.endCurrent()

        if event.type == pygame.MOUSEMOTION:
            if twodButton.isOver(pos):
                twodButton.color = (255, 0, 0)
            else:
                twodButton.color = (180, 0, 0)
            if threedButton.isOver(pos):
                threedButton.color = (255, 0, 0)
            else:
                threedButton.color = (180, 0, 0)
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)
def box_text_input(event, input_boxes):
    if event.type == pygame.KEYDOWN:            
        for box in input_boxes.keys():
            if box.active:
                if event.key == pygame.K_RETURN:
                    print(box.text)
                    box.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    box.text = box.text[:-1]
                else:
                    try:
                        _=float(event.unicode)
                        box.text += event.unicode    
                    except:
                        if event.unicode == "." or event.unicode == "-":
                            temp_text = box.text
                            temp_text +=event.unicode
                            try:
                                float(temp_text)
                                box.text +=event.unicode   
                            except:
                                if len(box.text) == 0:
                                    if event.unicode == "-" or event.unicode=='.':
                                        box.text +=event.unicode 


def tut2D_step1_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-1",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["The first step to draw a 2-d Mohr circle ",
              "for the given stress state is to draw",
              "the points corresponding to the stresses" ,
              "On a graph, Plot: ",
              "(sigma_xx, -tau_xy) & (sigma_yy, tau_xy)"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_stress_input_window_check.makeCurrent()
                tut2D_step1_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step1_window_check.endCurrent()
                tut2D_step2_window_check.makeCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), 
                                                    float(sigma_yy_tut.text),float(tau_xy_tut.text))
                req_mohr.ndims = 2
                req_mohr.plot_init_pts()
def tut2D_step2_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-2",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["The next step to draw a 2-d Mohr circle ",
              "for the given stress state is to draw",
              "is to join the points plotted using a ",
              "straight line. Mark the point where the ",
              "line intersects X-axis as the center of ",
              "the circle" ,]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step1_window_check.makeCurrent()
                tut2D_step2_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step2_window_check.endCurrent()
                tut2D_step3_window_check.makeCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), 
                                                    float(sigma_yy_tut.text),float(tau_xy_tut.text))
                req_mohr.ndims = 2
                req_mohr.plot_cent()
def tut2D_step3_window(screen, prev_win, windows):
    global angle_check
    global sigma1, sigma2, curr_angle
    Big_font = game_font(60)
    Small_font = game_font(25)
    extra_small_font = game_font(15)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-3",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the center and radius being ",
              "the distance between the center and one ",
              "of the plotted points, draw a circle.",
              "Thus you get your Mohr's Circle",
              "The points where the circle cuts the X-axis",
              "are the principal stresses."]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    xButton = nextButton
    if angle_check==0:
        xButton = finishButton
    xButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))


    try:
        mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= 0, 
                                                σxy= float(tau_xy_tut.text), σyz=0, σzx=0)
        mohr_2d.ndims = 2
        mohr_2d.isGraph = False
        if(angle_gen.text!=''):
            mohr_2d.isAngle_stress = True
            mohr_2d.reqAngle_stress_2d = float(angle_gen.text)
        _,sig,_,_,_,curr_angle = mohr_2d.stress_execute()
        sigma1, sigma2 = sig[0][0], sig[1][0]
        
        curr_angle = round(np.rad2deg(curr_angle),2)
        answer_txt = "sigma_1 : "+str(sigma1)+", sigma_2 : "+str(sigma2) + ", phi : "+str(curr_angle)+" deg"
        answer_txt = extra_small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (50, 480))  
    except ValueError:
        # print(e)
        answer_txt = "sigma_1 :   sigma_2 :   phi"
        answer_txt = extra_small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (50, 480))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step2_window_check.makeCurrent()
                tut2D_step3_window_check.endCurrent()
            if xButton.isOver(pos):
                if xButton==nextButton:
                    tut2D_step3_window_check.endCurrent()
                    tut2D_step4_window_check.makeCurrent()
                else:
                    tut2D_step3_window_check.endCurrent()
                    tut2D_final_window_check.makeCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), 
                                                    float(sigma_yy_tut.text),float(tau_xy_tut.text))
                req_mohr.ndims = 2
                req_mohr.plot_circle()

def tut2D_step4_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-4",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the center and radius being ",
              "To find the values of stress at an angle", 
              "say theta. Rotate the line about the center",
              "by an angle of 2*theta.", " ",
              "NOTE: the rotation should be in anticlockwise ",
              "direction with the angle is positive and",
              "clockwise if the angle is negative"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step3_window_check.makeCurrent()
                tut2D_step4_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut2D_step5_window_check.makeCurrent()
                tut2D_step4_window_check.endCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), 
                                                    float(sigma_yy_tut.text),float(tau_xy_tut.text))
                req_mohr.angle2d= float(angle_tut.text)
                req_mohr.ndims = 2
                req_mohr.plot_angle2d()
def tut2D_step5_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-5",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the center and radius being ",
              "Thus the new line has its end-points on",
              "the circle. These endpoints denote the new",
              "(sigma_xx, -tau_xy) and (sigma_yy, tau_xy)",
              " ",
              "Thus you get the required values of stress",
              "at the required angle using Mohr's Circle!!!"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    finishButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut2D_step4_window_check.makeCurrent()
                tut2D_step5_window_check.endCurrent()
            if finishButton.isOver(pos):
                tut2D_final_window_check.makeCurrent()
                tut2D_step5_window_check.endCurrent()
            if graphButton.isOver(pos):
                req_mohr = Stress_MohrCircle(float(sigma_xx_tut.text), 
                                                    float(sigma_yy_tut.text),float(tau_xy_tut.text))
                # req_mohr.angle = float(angle_tut.text)
                req_mohr.ndims = 2
                # req_mohr.plot_angle2d()
                req_mohr.isAngle_stress = True
                req_mohr.reqAngle_stress_2d = float(angle_tut.text)
                req_mohr.isGraph = True
                req_mohr.stress_execute()
def tut2D_final_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("Congratulations!!",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the center and radius being ",
              "you have learnt to draw a Mohr Circle",
              "and find the component of stress at various",
              "angles.",
              "Try out the Quiz! or Explore in General Mode"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    back_to_homeButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                windows[prev_win][1].makeCurrent()
                tut2D_final_window_check.endCurrent()
            if back_to_homeButton.isOver(pos):
                enterWindow_check.makeCurrent()
                tut2D_final_window_check.endCurrent()
def tut2D_stress_input_window(screen, prev_win, windows): 
    global angle_check
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_tut:"sigma_xx", sigma_yy_tut:"sigma_yy", tau_xy_tut:"tau_xy", angle_tut:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 2- D Mode",1, (0,0,0))
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
    screen.blit(head_text, (360, 100))  
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tutorialwindow_check.makeCurrent()
                tut2D_stress_input_window_check.endCurrent()
            if nextButton.isOver(pos):
                try:
                    mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= 0, 
                                                σxy= float(tau_xy_tut.text), σyz=0, σzx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = False
                    if(angle_tut.text!=''):
                        mohr_2d.isAngle_stress = True
                        angle_check = 1
                        mohr_2d.reqAngle_stress_2d = float(angle_tut.text)
                    else:
                        angle_check = 0
                    mohr_2d.stress_execute()
                    tut2D_stress_input_window_check.endCurrent()
                    tut2D_step1_window_check.makeCurrent()
                except:
                    tut2D_stress_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)

        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)


    for box in input_boxes.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)
def tut3D_step1_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-1",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["The first step to draw a 3-d Mohr circle ",
              "for the given stress state is to find the",
              "principle stresses. we find it by first ",
              "placing the stresses in a stress-tensor" ,
            ]
    tens_init_text = ["[sig_xx tau_xy tau_xz",
                       " tay_xy sig_yy tau_yz    =",
                       " tau_xz tau_yz sig_zz]"]
    user_tens_text = ["["+str(sigma_xx_tut.text) +" "+ str(tau_xy_tut.text) +" " +str(tau_zx_tut.text),
                       " "+str(tau_xy_tut.text) +" "+ str(sigma_yy_tut.text) +" " +str(tau_yz_tut.text),
                       " "+str(tau_zx_tut.text) +" "+ str(tau_yz_tut.text) +" " +str(sigma_zz_tut.text)+"]"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=30
    count=0
    for text in tens_init_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(30, 350+count))
        count+=30
    count = 0
    for text in user_tens_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(500, 350+count))
        count+=30
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_stress_input_window_check.makeCurrent()
                tut3D_step1_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut3D_step1_window_check.endCurrent()
                tut3D_step2_window_check.makeCurrent()
def tut3D_step2_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    extra_small_font = game_font(15)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-2",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["After placing the values appropriately,",
              "the next step involves solving for eigen",
              "values. So, the Characteristic Equation is:",
              "lamb^3 - I1*lamb^2 + I2*lamb -I3 = 0"]
    formula_text = ["where, I1, I2, I3 are given by: " ,
              "I1 = sig_xx + sig_yy + sig_zz",
              "I2 = sig_xx*sig_yy + sig_xx*sig_zz + sig_yy*sig_zz - tau_xy^2 - tau_xz^2 - tau_yz^2",
              "I3 = determinant(Tensor)"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    count = 0
    for text in formula_text:
        text = extra_small_font.render(text,1,(0,0,0))
        screen.blit(text,(40, 400+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step1_window_check.makeCurrent()
                tut3D_step2_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut3D_step2_window_check.endCurrent()
                tut3D_step3_window_check.makeCurrent()

def tut3D_step3_window(screen, prev_win, windows):
    global angle_check
    Big_font = game_font(60)
    Small_font = game_font(25)
    extra_small_font = game_font(18)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-3",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    m = tut_Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= float(sigma_zz_tut.text), 
                              σxy= float(tau_xy_tut.text), σyz=float(tau_yz_tut.text), σzx=float(tau_zx_tut.text))
    m.ndims = 3
    Is = m.get_I_values()
    tut_text=["Now, using the center and radius being ",
              "Therefore, the corresponding values are : ",
              "I1 = "+str(round(Is[0],3)),
              "I2 = "+str(round(Is[1],3)),
              "I3 = "+str(round(Is[2],3)),
              ]
    eqn_text = ["The next step would be to calculate the",
                "values of lamb from previous slide.",
                "our equation becomes : ",
                "lamb^3 - ("+str(round(Is[0],3)) + ")*lamb^2 + "+str(round(Is[1],3))+"*lamb -("+str(round(Is[2],3))+") = 0",
                ]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    count = 0
    for text in eqn_text:
        text = extra_small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 410+count))
        count+=30
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step2_window_check.makeCurrent()
                tut3D_step3_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut3D_step3_window_check.endCurrent()
                tut3D_step4_window_check.makeCurrent()

def tut3D_step4_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-4",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    m = tut_Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= float(sigma_zz_tut.text), 
                              σxy= float(tau_xy_tut.text), σyz=float(tau_yz_tut.text), σzx=float(tau_zx_tut.text))
    m.ndims = 3
    eigen = m.get_princip_values()
    prin_stress = np.sort(eigen)[::-1]
    tut_text=["Now, using the center and radius being ",
              "Solving the equation gives us : ", 
              "lamb = " + str(eigen[0]) + ", lamb = " + str(eigen[1]) + ", lamb = " + str(eigen[2]),
              " ", "Arrange the values such that sig_1",
              "is the largest and sig_3 is the least",
              "sig_1, sig_2, sig_3 are principle stresses",
              "sig_1 = " + str(prin_stress[0]) + ", sig_2 = " + str(prin_stress[1]) + ", sig_3 = " + str(prin_stress[2]),]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(65, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step3_window_check.makeCurrent()
                tut3D_step4_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut3D_step5_window_check.makeCurrent()
                tut3D_step4_window_check.endCurrent()


def tut3D_step5_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 2-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-5",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the principle stresses, ",
              "Plot the stresses calculated on the X-axis",
              "Find the midpoint between each of the three",
              "points",
              ]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    nextButton.draw(screen,(0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step4_window_check.makeCurrent()
                tut3D_step5_window_check.endCurrent()
            if nextButton.isOver(pos):
                tut3D_step6_window_check.makeCurrent()
                tut3D_step5_window_check.endCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), float(sigma_yy_tut.text),float(tau_xy_tut.text),
                                                 float(sigma_zz_tut.text), float(tau_yz_tut.text), float(tau_zx_tut.text))
                req_mohr.ndims = 3
                req_mohr.plot_cent()
def tut3D_step6_window(screen, prev_win, windows):
    global angle_check
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-6",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Using the centers, and the corresponding ",
              "principle stresse, draw circles with radii",
              "being distance between the centers and their",
              "corresponding principle stresses.",
              ]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    xButton = nextButton
    if angle_check==0:
        xButton = finishButton
    xButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step5_window_check.makeCurrent()
                tut3D_step6_window_check.endCurrent()
            if xButton.isOver(pos):
                if xButton == nextButton:
                    tut3D_step7_window_check.makeCurrent()
                    tut3D_step6_window_check.endCurrent()
                else:
                    tut3D_final_window_check.makeCurrent()
                    tut3D_step6_window_check.endCurrent()
            if graphButton.isOver(pos):
                req_mohr = tut_Stress_MohrCircle(float(sigma_xx_tut.text), float(sigma_yy_tut.text),float(tau_xy_tut.text),
                                                 float(sigma_zz_tut.text), float(tau_yz_tut.text), float(tau_zx_tut.text))
                req_mohr.ndims = 3
                req_mohr.plot_circle_3d()  
                
def tut3D_step7_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    extra_small_font = game_font(18)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("STEP-7",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    l = np.cos(np.deg2rad(float(angle1_tut.text)))
    m = np.cos(np.deg2rad(float(angle2_tut.text)))
    n = np.sqrt(1-l**2-m**2)
    if(n==None):
        n=0
    tut_text=["To find the the value of stresses on plane",
              "whose normal's direction vector is (l,m,n)",
              "l = cos("+str(angle1_tut.text)+") = "+str(round(l,3)),
              "m = cos("+str(angle2_tut.text)+") = "+str(round(m,3)),
              "n = sqrt(1 - l^2 -m^2) =  "+str(round(n,3)),
              ]
    tut2_text=["use the following formula to obtain normal",
               "and shear stress : ",
               "sig_normal = l^2*sig_1+m^2*sig_2+n^2*sig_3",
               "sig_shear = l^2*sig_1^2 + m^2*sig_2^2 + n^2*sig_3^2 - sig_normal^2",
               "PLot the point (sig_normal, sig_shear)"
               ]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(70, 200+count))
        count+=40
    count =0
    for text in tut2_text:
        text = extra_small_font.render(text,1,(0,0,0))
        screen.blit(text,(40, 400+count))
        count+=25
    backButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    finishButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tut3D_step6_window_check.makeCurrent()
                tut3D_step7_window_check.endCurrent()
            if finishButton.isOver(pos):
                tut3D_final_window_check.makeCurrent()
                tut3D_step7_window_check.endCurrent()
            if graphButton.isOver(pos):
                mohr_3d = Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= float(sigma_zz_tut.text), 
                                                σxy= float(tau_xy_tut.text), σyz= float(tau_yz_tut.text),σzx= float(tau_zx_tut.text))
                mohr_3d.ndims = 3
                mohr_3d.isGraph = True
                if(angle1_tut.text!='' and angle2_tut.text!= ''):
                    angle_check = 1
                    mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_tut.text))),3), 
                                                    round(np.cos(np.deg2rad(float(angle2_tut.text))),3), 0]
                    mohr_3d.isAngle_stress = True
                mohr_3d.stress_execute()

def tut3D_final_window(screen, prev_win, windows):
    Big_font = game_font(60)
    Small_font = game_font(25)
    mid_font = game_font(40)
    # print(sigma_xx_tut.text, sigma_yy_tut.text, tau_xy_tut.text, angle_tut.text)
    head_text = Big_font.render("Tutorial 3-D Mode",1, (0,0,0))
    mid_text = mid_font.render("Congratulations!!",1,(0,0,0))
    screen.blit(head_text, (80, 70))
    screen.blit(mid_text, (80, 150))
    tut_text=["Now, using the center and radius being ",
              "you have learnt to draw a Mohr Circle",
              "and find the component of stress at various",
              "angles.",
              "Try out the Quiz! or Explore in General Mode"]
    count =0 
    for text in tut_text:
        text = Small_font.render(text,1,(0,0,0))
        screen.blit(text,(120, 200+count))
        count+=40
    backButton.draw(screen, (0,0,0))
    back_to_homeButton.draw(screen, (0,0,0))
    graphButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                windows[prev_win][1].makeCurrent()
                tut3D_final_window_check.endCurrent()
            if back_to_homeButton.isOver(pos):
                enterWindow_check.makeCurrent()
                tut3D_final_window_check.endCurrent()

def tut3D_stress_input_window(screen, prev_win, windows): 
    global angle_check
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_tut:"sigma_xx", sigma_yy_tut:"sigma_yy", tau_xy_tut:"tau_xy", 
                   sigma_zz_tut:"sigma_zz", tau_yz_tut:"tau_yz", tau_zx_tut:"tau_zx",
                   angle1_tut:"Angle x", angle2_tut:'Angle y', angle3_tut:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("Tutorial 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))

    screen.blit(head_text, (360, 100))  
    backButton.draw(screen, (0,0,0))
    enterButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:  
            global running              
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                tutorialwindow_check.makeCurrent()
                tut3D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Stress_MohrCircle(σxx= float(sigma_xx_tut.text), σyy= float(sigma_yy_tut.text),σzz= float(sigma_zz_tut.text), 
                                                σxy= float(tau_xy_tut.text), σyz= float(tau_yz_tut.text),σzx= float(tau_zx_tut.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = False
                    if(angle1_tut.text!='' and angle2_tut.text!= ''):
                        angle_check = 1
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_tut.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_tut.text))),3), 0]
                        mohr_3d.isAngle_stress = True
                    mohr_3d.stress_execute()
                    tut3D_stress_input_window_check.endCurrent()
                    tut3D_step1_window_check.makeCurrent()
                except Exception as e:
                    print(e)
                    tut3D_stress_input_window_check.endCurrent()
                    incompatible_input_window_check.makeCurrent()                    
            for box in input_boxes.keys():
                if box.render().collidepoint(event.pos):
                    print("click")
                    box.active = True
                else:
                    box.active = False
        box_text_input(event, input_boxes)


        if event.type == pygame.MOUSEMOTION:
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)


    for box in input_boxes.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)