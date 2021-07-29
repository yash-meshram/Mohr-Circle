
import window_types.mohr_quiz as mohr_quiz
import window_types.mohr_general as mohr_general
import window_types.pop_up as pop_up
import window_types.mohr_initial as mohr_initial
import window_types.mohr_tutorial as mohr_tutorial
from utilities.mohr_screen import *

windows = {"startwindow" : [mohr_initial.startwindow,startwindow_check],
            "enterwindow" : [mohr_initial.enterwindow, enterWindow_check],
            "aboutwindow" : [mohr_initial.aboutwindow, aboutwindow_check],

            "generalwindow" : [ mohr_general.generalwindow,generalwindow_check],
            "gen2D_stress_input_window" : [mohr_general.gen2D_stress_input_window, gen2D_stress_input_window_check],
            "gen3D_stress_input_window" :[mohr_general.gen3D_stress_input_window, gen3D_stress_input_window_check],
            "gen2D_strain_input_window" : [mohr_general.gen2D_strain_input_window, gen2D_strain_input_window_check],
            "gen3D_strain_input_window" :[mohr_general.gen3D_strain_input_window, gen3D_strain_input_window_check],
            "gen_stress_strain_window_gen" :[mohr_general.gen_stress_strain_window, gen_stress_strain_window_check],
            
            "tutorialwindow" : [ mohr_tutorial.tutorialwindow,tutorialwindow_check],
            "tut2D_stress_input_window" : [mohr_tutorial.tut2D_stress_input_window, tut2D_stress_input_window_check],
            "tut3D_stress_input_window" :[mohr_tutorial.tut3D_stress_input_window, tut3D_stress_input_window_check],
            # "tut2D_strain_input_window" : [mohr_tutorial.tut2D_strain_input_window, tut2D_strain_input_window_check],
            # "tut3D_strain_input_window" :[mohr_tutorial.tut3D_strain_input_window, tut3D_strain_input_window_check],
            # "tut_stress_strain_window_gen" :[mohr_tutorial.tut_stress_strain_window, tut_stress_strain_window_check],
            "tut2D_step1_window" :[mohr_tutorial.tut2D_step1_window, tut2D_step1_window_check],
            "tut2D_step2_window" :[mohr_tutorial.tut2D_step2_window, tut2D_step2_window_check],
            "tut2D_step3_window" :[mohr_tutorial.tut2D_step3_window, tut2D_step3_window_check],
            "tut2D_step4_window" :[mohr_tutorial.tut2D_step4_window, tut2D_step4_window_check],
            "tut2D_step5_window" :[mohr_tutorial.tut2D_step5_window, tut2D_step5_window_check],
            "tut2D_final_window" :[mohr_tutorial.tut2D_final_window, tut2D_final_window_check],
            
            "tut3D_step1_window" :[mohr_tutorial.tut3D_step1_window, tut3D_step1_window_check],
            "tut3D_step2_window" :[mohr_tutorial.tut3D_step2_window, tut3D_step2_window_check],
            "tut3D_step3_window" :[mohr_tutorial.tut3D_step3_window, tut3D_step3_window_check],
            "tut3D_step4_window" :[mohr_tutorial.tut3D_step4_window, tut3D_step4_window_check],
            "tut3D_step5_window" :[mohr_tutorial.tut3D_step5_window, tut3D_step5_window_check],
            "tut3D_step6_window" :[mohr_tutorial.tut3D_step6_window, tut3D_step6_window_check],
            "tut3D_step7_window" :[mohr_tutorial.tut3D_step7_window, tut3D_step7_window_check],
            
            "tut3D_final_window" :[mohr_tutorial.tut3D_final_window, tut3D_final_window_check],
            
            "quizwindow":[mohr_quiz.quizwindow,quizwindow_check],
            "quizwindow_2d":[mohr_quiz.quizwindow_2d,quizwindow_2d_check],
            "quizwindow_3d":[mohr_quiz.quizwindow_3d,quizwindow_3d_check],
            "quizwindow_concept":[mohr_quiz.quizwindow_concept,quizwindow_concept_check],
            "quiz_end_window":[mohr_quiz.quiz_end_window,quiz_end_window_check],
            "eval_window":[mohr_quiz.eval_window,eval_window_check],
            "incompatible_input_window":[pop_up.incompatible_input_window,incompatible_input_window_check]}