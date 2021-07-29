
import pygame
import numpy as np
from utilities.mohr_fonts import game_font
from utilities.mohr_user_input import *
from utilities.mohr_checkbox import *
from utilities.mohr_concept_questions import concept_quest
from MohrCircle_stress import Stress_MohrCircle
# from MohrCircle_strain import strain_execute
import random
from utilities.mohr_screen import *
import time
# quiz_question_type = ['2-D', '2-D','3-D','3-D', 'concept']
quiz_question_type = ['2-D','2-D','3-D','3-D','concept','concept','concept']
# quiz_question_type = ['concept']*10
quest_nos = [1,2,3,4,5,6,7,8,9,10]
user_concept_answer = -1
quest_index = -1
curr_question_type = None
correct_answer = None
userScore = 0

def quizwindow(screen, prev_win, windows):
    Big_font = game_font(80)
    Small_font = game_font(20)
    text = Big_font.render("Quiz Mode",1, (0,0,0))
    screen.blit(text, (150, 200))
    backButton.draw(screen, (0,0,0))
    startButton.draw(screen,(0,0,0))

    global curr_question_type,quiz_question_type, sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx,quest_nos,quest_index
    # print(len(quiz_question_type))
    random.shuffle(quiz_question_type)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if backButton.isOver(pos):
                enterWindow_check.makeCurrent()
                quizwindow_check.endCurrent()

            if startButton.isOver(pos):
                if quiz_question_type[0] == '2-D':
                    sigma_xx = round(random.randint(-30,30), 2)
                    sigma_yy = round(random.randint(-30,30), 2)
                    tau_xy = round(random.randint(-30,30), 2)
                    sigma_zz = 0
                    tau_yz = 0
                    tau_zx = 0
                    quiz_question_type = quiz_question_type[1:]
                    quizwindow_2d_check.makeCurrent()
                    quizwindow_check.endCurrent()
                elif quiz_question_type[0] == '3-D':
                    sigma_xx = round(random.randint(-30,30), 2)
                    sigma_yy = round(random.randint(-30,30), 2)
                    sigma_zz = round(random.randint(-30,30), 2)
                    tau_xy = round(random.randint(-30,30), 2)
                    tau_yz = round(random.randint(-30,30), 2)
                    tau_zx = round(random.randint(-30,30), 2)
                    quiz_question_type = quiz_question_type[1:]
                    quizwindow_3d_check.makeCurrent()
                    quizwindow_check.endCurrent()
                elif quiz_question_type[0] == 'concept':   
                    quiz_question_type = quiz_question_type[1:]
                    quest_index = random.randint(0,len(quest_nos)-1)
                    quizwindow_concept_check.makeCurrent()
                    quizwindow_check.endCurrent()
                

        if event.type == pygame.MOUSEMOTION:
            if startButton.isOver(pos):
                startButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)
            if backButton.isOver(pos):
                backButton.color = (255, 0, 0)
            else:
                backButton.color = (180, 0, 0)

def quiz_button_loop(event, x_button, current_window_check, ans_box):
    Small_font = game_font(20)
    global correct_answer,curr_question_type,quiz_question_type,sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx
    pos = pygame.mouse.get_pos()

    if event.type == pygame.QUIT:  
        global running              
        running = False
    if event.type == pygame.MOUSEBUTTONDOWN:

        if x_button.isOver(pos):
            current_window_check.endCurrent()
            eval_window_check.makeCurrent()
            
        for box in ans_box.keys():
            if box.render().collidepoint(event.pos):
                box.active = True
            else:
                box.active = False
    if event.type == pygame.KEYDOWN:
        for box in ans_box.keys():
            if box.active:
                if event.key == pygame.K_RETURN:
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
    if event.type == pygame.MOUSEMOTION:
        if x_button.isOver(pos):
            x_button.color = (255, 0, 0)
        else:
            x_button.color = (180, 0, 0)
    return ans_box 

show_graph = 0
def eval_window(screen, prev_win, windows):
    global userScore,show_graph,correct_answer,curr_question_type,quiz_question_type, user_concept_answer
    global sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx, quest_nos, quest_index
    if curr_question_type!='concept':
        mohr_2d = Stress_MohrCircle(σxx= sigma_xx, σyy= sigma_yy,σzz= sigma_zz, σxy= tau_xy, σyz= tau_yz, σzx= tau_zx)
        mohr_2d.ndims = 2
        mohr_3d = Stress_MohrCircle(σxx= sigma_xx, σyy= sigma_yy,σzz= sigma_zz, σxy= tau_xy, σyz= tau_yz, σzx= tau_zx)
        mohr_3d.ndims = 3
    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    Big_font = game_font(40)
    Small_font = game_font(20)
    if(curr_question_type!="concept"):
        graphButton.draw(screen, (0,0,0))
    isCorrect = False

    if show_graph == 0:
        if curr_question_type!='concept':
            if curr_question_type=='2-D':
                mohr_2d.isGraph = False
                correct_answer=mohr_2d.stress_execute()
                correct_answer = correct_answer[0]

            elif curr_question_type=='3-D':
                mohr_2d.isGraph = False
                correct_answer=mohr_3d.stress_execute()
                correct_answer = correct_answer[0]        

    try:
        if curr_question_type == "2-D":
            if correct_answer[0][0] < float(C1_gen.text) + 0.5 and correct_answer[0][0] > float(C1_gen.text) - 0.5:
                
                isCorrect = True
                if show_graph ==0 :
                    userScore +=5
        elif curr_question_type == "3-D":
            user_answer = [[float(C1_gen.text)],[float(C2_gen.text)],[float(C3_gen.text)]]
            counter = 0
            for k in user_answer:
                for l in correct_answer:
                    if k[0] <l[0] + 0.5 and k[0] > l[0]-0.5:
                        counter+=1
                        break
            if counter==3:
                isCorrect = True
                if show_graph == 0:
                    userScore +=5
        elif curr_question_type == 'concept':
            if(concept_quest[quest_nos[quest_index]][2] == user_concept_answer):
                isCorrect = True
                if show_graph == 0:
                    userScore+=5
    except:
        pass
    show_graph+=1
    if(isCorrect):
            text = Big_font.render("CORRECT :)", 1, (0,0,0))
            screen.blit(text, (70, 250))
    else:
            text = Big_font.render("WRONG :(", 1, (0,0,0))
            screen.blit(text, (70, 250))
            
    if curr_question_type=='concept':
        line_brk = 0
        exp_text = concept_quest[quest_nos[quest_index]][3]
        # print(exp_text)
        for exp in exp_text:
            exp = Small_font.render(exp, 1, (0,0,0))
            screen.blit(exp, (70, 300 + line_brk))
            line_brk+=20

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.MOUSEMOTION:
            if(curr_question_type!="concept"):
                if graphButton.isOver(pos):
                    graphButton.color = (255, 0, 0)
                else:
                    graphButton.color = (180, 0, 0)
                
            if x_button.isOver(pos):
                x_button.color = (255, 0, 0)
            else:
                x_button.color = (180, 0, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if graphButton.isOver(pos):
                if curr_question_type!='concept':
                    if curr_question_type=='2-D':
                        mohr_2d.isGraph = True
                        mohr_2d.stress_execute()

                    elif curr_question_type=='3-D':
                        mohr_3d.isGraph = True
                        mohr_3d.stress_execute()
            
            if x_button.isOver(pos):
                if len(quiz_question_type) > 0:
                    # print(quiz_question_type[0])
                    show_graph = 0
                    if quiz_question_type[0] == '2-D':
                        sigma_xx = round(random.randint(-30,30), 2)
                        sigma_yy = round(random.randint(-30,30), 2)
                        tau_xy = round(random.randint(-30,30), 2)
                        sigma_zz = 0
                        tau_yz = 0
                        tau_zx = 0
                        quiz_question_type = quiz_question_type[1:]
                        eval_window_check.endCurrent()
                        quizwindow_2d_check.makeCurrent()    
                    elif quiz_question_type[0] == '3-D':
                        sigma_xx = round(random.randint(-30,30), 2)
                        sigma_yy = round(random.randint(-30,30), 2)
                        sigma_zz = round(random.randint(-30,30), 2)
                        tau_xy = round(random.randint(-30,30), 2)
                        tau_yz = round(random.randint(-30,30), 2)
                        tau_zx = round(random.randint(-30,30), 2)
                        quiz_question_type = quiz_question_type[1:]
                        eval_window_check.endCurrent()
                        quizwindow_3d_check.makeCurrent()
                    elif quiz_question_type[0] == 'concept':  
                        user_concept_answer = -1 
                        quiz_question_type = quiz_question_type[1:]
                        quest_nos.remove(quest_nos[quest_index])
                        print(quest_nos)
                        quest_index = random.randint(0,len(quest_nos)-1)
                        eval_window_check.endCurrent()
                        quizwindow_concept_check.makeCurrent()
                else:
                    eval_window_check.endCurrent()
                    quiz_end_window_check.makeCurrent()


        
def quizwindow_2d(screen, prev_win, windows):
    clock = pygame.time.Clock()
    Big_font = game_font(40)
    Small_font = game_font(20)
    text = Big_font.render("Quiz on 2-D Mohr circle",1, (0,0,0))
    screen.blit(text, (100, 70))
    text = Small_font.render("Draw the mohr circle for the following 2-D stress field",1, (0,0,0))
    screen.blit(text, (30, 150))

    ans_boxes_2d = {C1_gen:"C1"}
    for box in ans_boxes_2d.keys():
        box_text = Small_font.render(ans_boxes_2d[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    global curr_question_type,quiz_question_type,sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx
    # print(len(quiz_question_type))
    curr_question_type = '2-D'

    text = Small_font.render("sigma_xx = ",1, (0,0,0))
    screen.blit(text, (50, 200))
    text = Small_font.render("sigma_yy = ",1, (0,0,0))
    screen.blit(text, (50, 250))
    text = Small_font.render("tau_xy = ",1, (0,0,0))
    screen.blit(text, (50, 300))

    text = Small_font.render(str(sigma_xx) , 1, (0,0,0))
    screen.blit(text, (180, 200))
    text = Small_font.render(str(sigma_yy) ,1, (0,0,0))
    screen.blit(text, (180, 250))
    text = Small_font.render(str(tau_xy) ,1, (0,0,0))
    screen.blit(text, (180, 300))

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    for event in pygame.event.get():
        ans_boxes_2d=quiz_button_loop(event, x_button, quizwindow_2d_check, ans_boxes_2d)          

    for box in ans_boxes_2d.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)

def quizwindow_3d(screen, prev_win, windows):
    clock = pygame.time.Clock()
    Big_font = game_font(40)
    Small_font = game_font(20)
    text = Big_font.render("Quiz on 3-D Mohr circle",1, (0,0,0))
    screen.blit(text, (100, 70))
    text = Small_font.render("Draw the mohr circle for the following 3-D stress field",1, (0,0,0))
    screen.blit(text, (30, 150))

    ans_boxes_3d = {C1_gen:"C1", C2_gen:"C2", C3_gen:"C3"}
    for box in ans_boxes_3d.keys():
        box_text = Small_font.render(ans_boxes_3d[box]+":",1,(0,0,0))
        screen.blit(box_text,(box.x - 80, box.y))

    global curr_question_type,quiz_question_type,sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx
    # print(len(quiz_question_type  ))
    curr_question_type = '3-D'
    
    text = Small_font.render("sigma_xx = ",1, (0,0,0))
    screen.blit(text, (50, 200))
    text = Small_font.render("sigma_yy = ",1, (0,0,0))
    screen.blit(text, (50, 250))
    text = Small_font.render("sigma_zz = ",1, (0,0,0))
    screen.blit(text, (50, 300))
    text = Small_font.render("tau_xy = ",1, (0,0,0))
    screen.blit(text, (50, 350))
    text = Small_font.render("tau_yz = ",1, (0,0,0))
    screen.blit(text, (50, 400))
    text = Small_font.render("tau_zx = ",1, (0,0,0))
    screen.blit(text, (50, 450))

    text = Small_font.render(str(sigma_xx) , 1, (0,0,0))
    screen.blit(text, (180, 200))
    text = Small_font.render(str(sigma_yy) ,1, (0,0,0))
    screen.blit(text, (180, 250))
    text = Small_font.render(str(sigma_zz) ,1, (0,0,0))
    screen.blit(text, (180, 300))
    text = Small_font.render(str(tau_xy) ,1, (0,0,0))
    screen.blit(text, (180, 350))
    text = Small_font.render(str(tau_yz) ,1, (0,0,0))
    screen.blit(text, (180, 400))
    text = Small_font.render(str(tau_zx) ,1, (0,0,0))
    screen.blit(text, (180, 450))

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    for event in pygame.event.get():
        ans_boxes_3d = quiz_button_loop(event, x_button, quizwindow_3d_check, ans_boxes_3d)
        
    for box in ans_boxes_3d.keys():
        txt_surface = Small_font.render(box.text, True, box.color)
        width = max(200, txt_surface.get_width()+10)
        box.render().w = width
        screen.blit(txt_surface, (box.x+5, box.y+5))
        pygame.draw.rect(screen, box.color, box.render(), 2)
    
    clock.tick(30)

def quizwindow_concept(screen, prev_win, windows):
    global quiz_question_type,sigma_xx, sigma_yy, sigma_zz, tau_xy, tau_yz, tau_zx, quest_nos,quest_index, user_concept_answer, curr_question_type
    # print(len(quiz_question_type))
    Big_font = game_font(40)
    Small_font = game_font(15)
    text = Big_font.render("Conceptual:",1, (0,0,0))
    screen.blit(text, (30, 70))
    count = 0
    for conc_text in concept_quest[quest_nos[quest_index]][0]:
        text = Small_font.render(conc_text,1, (0,0,0))
        screen.blit(text, (30, 150+count))
        count+=25

    x_button = nextButton
    if len(quiz_question_type) == 0:
        x_button = submitButton
    x_button.draw(screen, (0,0,0))

    check_boxes = [check1,check2,check3,check4]
    curr_question_type = 'concept'
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mcq_index = 0
            for check_box in check_boxes:
                if(check_box.render().collidepoint(event.pos)):
                    check_box.active = not check_box.active
                    if(check_box.active):
                        user_concept_answer=mcq_index
                else:
                    check_box.active = False
                mcq_index+=1
        quiz_button_loop(event, x_button, quizwindow_concept_check, {})
    
    opt_count = 0
    for check_box in check_boxes:
        text = Small_font.render(concept_quest[quest_nos[quest_index]][1][opt_count],1, (0,0,0))
        screen.blit(text, (check_box.x + 30, check_box.y))
        pygame.draw.rect(screen, check_box.color, check_box.render(),2)
        if(check_box.active==True):
            color, center, radius = check_box.draw_circ()
            pygame.draw.circle(screen,color,center, radius)
        opt_count +=1


def quiz_end_window(screen, prev_win, windows):
    global userScore, quiz_question_type
    Big_font = game_font(80)
    Small_font = game_font(20)
    text = Big_font.render("Quiz Over", 1, (0,0,0))
    screen.blit(text, (70, 250))
    text = Small_font.render ("Your Score : "+str(userScore),1, (0,0,0))
    screen.blit(text, (60, 400))
    quiz_question_type = ['concept']
    # enterButton.draw(screen, (0,0,0))
    back_to_homeButton.draw(screen,(0,0,0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            global running
            running = False

        if event.type == pygame.MOUSEMOTION:
            if back_to_homeButton.isOver(pos):
                back_to_homeButton.color = (255, 0, 0)
            else:
                back_to_homeButton.color = (180, 0, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_to_homeButton.isOver(pos):
                quiz_end_window_check.endCurrent()
                enterWindow_check.makeCurrent()
    