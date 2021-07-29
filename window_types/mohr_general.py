import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
import random
from utilities.mohr_screen import *
from MohrCircle_stress import Stress_MohrCircle
from MohrCircle_strain import Strain_MohrCircle
# from MohrCircle_strain import strain_execute
is_new_input = False
sigma1, sigma2, sigma3, curr_angle = None, None,None,None
epsi1, epsi2, epsi3 = None, None,None

stress_strain_win_select = [0,0]
def blitRotate(surf, image, pos, originPos, angle):

    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

def generalwindow(screen, prev_win, windows):
    Small_font = game_font(20)
    text = Small_font.render("General Mode",1, (0,0,0))
    screen.blit(text, (360, 100))

    twodButton.draw(screen, (0,0,0))
    threedButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if twodButton.isOver(pos):
                if(stress_strain_win_select[0] == 1):
                    gen2D_stress_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in stress 2-D Mode")
                else:
                    gen2D_strain_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in strain 2-D Mode")
            if threedButton.isOver(pos):
                if(stress_strain_win_select[0]==1):
                    gen3D_stress_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in 3-D Mode")
                else:
                    gen3D_strain_input_window_check.makeCurrent()
                    generalwindow_check.endCurrent()
                    print("Entering in strain 2-D Mode")
            if backButton.isOver(pos):
                gen_stress_strain_window_check.makeCurrent()
                generalwindow_check.endCurrent()

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
    global is_new_input
    if event.type == pygame.KEYDOWN:
        is_new_input = True
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
    else:
        is_new_input = False
def gen_stress_strain_window(screen, prev_win, windows):
    global stress_strain_win_select
    stress_strain_win_select = [0,0]
    stressButton.draw(screen, (0,0,0))
    strainButton.draw(screen, (0,0,0))
    # quizButton.draw(screen, (0,0,0))
    backButton.draw(screen, (0,0,0))
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stressButton.isOver(pos):
                generalwindow_check.makeCurrent()
                gen_stress_strain_window_check.endCurrent()
                stress_strain_win_select = [1,0]
                print(stress_strain_win_select)
                print("Entering in General strain Mode")
            if strainButton.isOver(pos):
                generalwindow_check.makeCurrent()
                gen_stress_strain_window_check.endCurrent()
                stress_strain_win_select = [0,1]
                print(stress_strain_win_select)
                print("Entering in General strain Mode")
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                gen_stress_strain_window_check.endCurrent()
        if event.type == pygame.MOUSEMOTION:
            if stressButton.isOver(pos):
                stressButton.color = (255, 0, 0)
            else:
                stressButton.color = (180, 0, 0)  
            if strainButton.isOver(pos):
                strainButton.color = (255, 0, 0)
            else:
                strainButton.color = (180, 0, 0) 
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

def gen2D_stress_input_window(screen, prev_win, windows): 
    global box_img, is_new_input, sigma1, sigma2, curr_angle
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"sigma_xx", sigma_yy_gen:"sigma_yy", tau_xy_gen:"tau_xy", angle_gen:"angle"}
    Small_font = game_font(20)
    # ang = 90
    image = pygame.image.load('Images/box_stress.png')
    w,h = image.get_size()
    pos = (550, 400)
    if(angle_gen.text in ["-","","+"]):
        blitRotate(screen, image,pos,(w/2,h/2), float(0))
    else:
        blitRotate(screen, image,pos,(w/2,h/2), float(angle_gen.text))
    # ang = 
    head_text = Small_font.render("General 2- D Mode",1, (0,0,0))
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
    
    try:
        if is_new_input == True: 
            mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_gen.text), σyy= float(sigma_yy_gen.text),σzz= 0, 
                                                    σxy= float(tau_xy_gen.text), σyz=0, σzx=0)
            mohr_2d.ndims = 2
            mohr_2d.isGraph = False
            if(angle_gen.text!=''):
                mohr_2d.isAngle_stress = True
                mohr_2d.reqAngle_stress_2d = float(angle_gen.text)
            _,sig,_,_,_,curr_angle = mohr_2d.stress_execute()
            sigma1, sigma2 = sig[0][0], sig[1][0]
            
            curr_angle = round(np.rad2deg(curr_angle),2)
            answer_txt = "sigma_1 : "+str(sigma1)+", sigma_2 : "+str(sigma2) + ", phi : "+str(curr_angle)+" deg"
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
        else:
            # print(curr_angle)
            answer_txt = "sigma_1 : "+str(sigma1)+", sigma_2 : "+str(sigma2) + ", phi : "+str(curr_angle) +" deg"
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
    except ValueError:
        # print(e)
        answer_txt = "sigma_1 :   sigma_2 :   phi"
        answer_txt = Small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (80, 540)) 

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
                generalwindow_check.makeCurrent()
                gen2D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                try:
                    mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_gen.text), σyy= float(sigma_yy_gen.text),σzz= 0, 
                                                σxy= float(tau_xy_gen.text), σyz=0, σzx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = True
                    if(angle_gen.text!=''):
                        mohr_2d.isAngle_stress = True
                        mohr_2d.reqAngle_stress_2d = float(angle_gen.text)
                    mohr_2d.stress_execute()
                    gen2D_stress_input_window_check.endCurrent()
                    gen2D_stress_input_window_check.makeCurrent()
                except:
                    gen2D_stress_input_window_check.endCurrent()
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


def gen3D_stress_input_window(screen, prev_win, windows): 
    global sigma1, sigma2, sigma3, is_new_input
    clock = pygame.time.Clock()
    input_boxes = {sigma_xx_gen:"sigma_xx", sigma_yy_gen:"sigma_yy", tau_xy_gen:"tau_xy", 
                   sigma_zz_gen:"sigma_zz", tau_yz_gen:"tau_yz", tau_zx_gen:"tau_zx",
                   angle1_gen:"Angle x", angle2_gen:'Angle y', angle3_gen:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("General 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
    
    try:
        if is_new_input == True: 
            mohr_2d = Stress_MohrCircle(σxx= float(sigma_xx_gen.text), σyy= float(sigma_yy_gen.text),σzz=float(sigma_zz_gen.text) , 
                                        σxy= float(tau_xy_gen.text), σyz=float(tau_yz_gen.text), σzx=float(tau_zx_gen.text))
            mohr_2d.ndims = 3
            mohr_2d.isGraph = False
            if(angle_gen.text!=''):
                mohr_2d.isAngle_stress = True
                # mohr_2d.reqAngle_stress_2d = float(angle_gen.text)
            _,sig,_,_ = mohr_2d.stress_execute()
            sigma1, sigma2, sigma3 = sig[0][0], sig[1][0], sig[2][0]
            answer_txt = "sigma_1 : "+str(sigma1)+"  sigma_2 : "+str(sigma2)+"  sigma_3 : "+str(sigma3)
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
        else:
            answer_txt = "sigma_1 : "+str(sigma1)+"  sigma_2 : "+str(sigma2)+"  sigma_3 : "+str(sigma3)
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
    except ValueError:
        # print(e)
        answer_txt = "sigma_1 :   sigma_2 :   sigma_3 : "
        answer_txt = Small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (80, 540))


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
                generalwindow_check.makeCurrent()
                gen3D_stress_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Stress_MohrCircle(σxx= float(sigma_xx_gen.text), σyy= float(sigma_yy_gen.text),σzz= float(sigma_zz_gen.text), 
                                                σxy= float(tau_xy_gen.text), σyz= float(tau_yz_gen.text),σzx= float(tau_zx_gen.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_gen.text!='' and angle2_gen.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_gen.text))),3), 
                                                      round(np.cos(np.deg2rad(float(angle2_gen.text))),3), 0]
                        mohr_3d.isAngle_stress = True
                    mohr_3d.stress_execute()
                    gen3D_stress_input_window_check.endCurrent()
                    gen3D_stress_input_window_check.makeCurrent()
                except Exception as e:
                    print(e)
                    gen3D_stress_input_window_check.endCurrent()
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

def gen2D_strain_input_window(screen, prev_win, windows): 
    global epsi1, epsi2, is_new_input, curr_angle
    clock = pygame.time.Clock()
    input_boxes = {epsi_xx_gen:"epsi_xx", epsi_yy_gen:"epsi_yy", epsi_xy_gen:"epsi_xy", angle_gen:"angle"}
    Small_font = game_font(20)
    head_text = Small_font.render("General 2- D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))
    image = pygame.image.load('Images/box_strain.png')
    w,h = image.get_size()
    pos = (550, 400)
    if(angle_gen.text in ["-","","+"]):
        blitRotate(screen, image,pos,(w/2,h/2), float(0))
    else:
        blitRotate(screen, image,pos,(w/2,h/2), float(angle_gen.text))
    try:
        if is_new_input == True: 
            mohr_2d = Strain_MohrCircle(εxx= float(epsi_xx_gen.text), εyy= float(epsi_yy_gen.text),εzz= 0, 
                                                    εxy= float(epsi_xy_gen.text), εyz=0, εzx=0)
            mohr_2d.ndims = 2
            mohr_2d.isGraph = False
            if(angle_gen.text!=''):
                mohr_2d.isAngle_strain = True
                mohr_2d.reqAngle_strain_2d = float(angle_gen.text)
            _,sig,_,_,_,curr_angle = mohr_2d.strain_execute()
            epsi1, epsi2 = sig[0][0], sig[1][0]
            curr_angle = round(np.rad2deg(curr_angle),2)
            answer_txt = "epsi_1 : "+str(epsi1)+"  epsi_2 : "+str(epsi2) + ", phi : "+str(curr_angle)+" deg"
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
        else:
            answer_txt = "epsi_1 : "+str(epsi1)+"  epsi_2 : "+str(epsi2)+ ", phi : "+str(curr_angle) +"deg"
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540))
    except:
        # print(e)
        answer_txt = "epsi_1 :   epsi_2 :   phi : "
        answer_txt = Small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (80, 540))

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
                generalwindow_check.makeCurrent()
                gen2D_strain_input_window_check.endCurrent()
                # global s
                # s = s - 1
                # A.pop()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_2d = Strain_MohrCircle(εxx= float(epsi_xx_gen.text), εyy= float(epsi_yy_gen.text),εzz= 0, 
                                                εxy= float(epsi_xy_gen.text), εyz=0, εzx=0)
                    mohr_2d.ndims = 2
                    mohr_2d.isGraph = True
                    if(angle_gen.text!=''):
                        mohr_2d.isAngle_strain = True
                        mohr_2d.reqAngle_strain_2d = float(angle_gen.text)
                    mohr_2d.strain_execute()
                    gen2D_strain_input_window_check.endCurrent()
                    gen2D_strain_input_window_check.makeCurrent()
                except:
                    gen2D_strain_input_window_check.endCurrent()
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


def gen3D_strain_input_window(screen, prev_win, windows): 
    global epsi1, epsi2, epsi3, is_new_input

    clock = pygame.time.Clock()
    input_boxes = {epsi_xx_gen:"epsi_xx", epsi_yy_gen:"epsi_yy", epsi_xy_gen:"epsi_xy",
                   epsi_zz_gen:"epsi_zz", epsi_yz_gen:"epsi_yz", epsi_zx_gen:"epsi_zx",
                   angle1_gen:"Angle x", angle2_gen:'Angle y', angle3_gen:'Angle z'}
    Small_font = game_font(20)
    head_text = Small_font.render("General 3-D Mode",1, (0,0,0))
    
    for box in input_boxes.keys():
        box_text = Small_font.render(input_boxes[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 120, box.y))


    try:
        if is_new_input == True: 
            mohr_2d = Strain_MohrCircle(εxx= float(epsi_xx_gen.text), εyy= float(epsi_yy_gen.text),εzz= float(epsi_zz_gen.text), 
                                        εxy= float(epsi_xy_gen.text), εyz=float(epsi_yz_gen.text), εzx=float(epsi_zx_gen.text))
            mohr_2d.ndims = 3
            mohr_2d.isGraph = False
            _,sig,_,_, = mohr_2d.strain_execute()
            epsi1, epsi2, epsi3 = sig[0][0], sig[1][0], sig[2][0]
            answer_txt = "epsi_1 : "+str(epsi1)+"  epsi_2 : "+str(epsi2) + "  epsi_3 : "+str(epsi3)
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540)) 
        else:
            answer_txt = "epsi_1 : "+str(epsi1)+"  epsi_2 : "+str(epsi2) + "  epsi_3 : "+str(epsi3)
            answer_txt = Small_font.render(answer_txt,1,(0,0,0))
            screen.blit(answer_txt, (80, 540))
    except ValueError:
        # print(e)
        answer_txt = "epsi_1 :   epsi_2 :   epsi_3:"
        answer_txt = Small_font.render(answer_txt,1,(0,0,0))
        screen.blit(answer_txt, (80, 540))
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
                generalwindow_check.makeCurrent()
                gen3D_strain_input_window_check.endCurrent()
            if enterButton.isOver(pos):
                mohrCircle_input = []
                try:
                    mohr_3d = Strain_MohrCircle(εxx= float(epsi_xx_gen.text), εyy= float(epsi_yy_gen.text),εzz= float(epsi_zz_gen.text), 
                                                εxy= float(epsi_xy_gen.text), εyz= float(epsi_yz_gen.text),εzx= float(epsi_zx_gen.text))
                    mohr_3d.ndims = 3
                    mohr_3d.isGraph = True
                    if(angle1_gen.text!='' and angle2_gen.text!= ''):
                        mohr_3d.reqAngle_normal_3d = [round(np.cos(np.deg2rad(float(angle1_gen.text))),3), 
                                                        round(np.cos(np.deg2rad(float(angle2_gen.text))),3), 0]
                        mohr_3d.isAngle_strain = True
                    mohr_3d.strain_execute()
                    gen3D_strain_input_window_check.endCurrent()
                    gen3D_strain_input_window_check.makeCurrent()
                except:
                    gen3D_strain_input_window_check.endCurrent()
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