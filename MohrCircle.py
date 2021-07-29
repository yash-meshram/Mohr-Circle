import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol


def Plot_Mohr_Circle(Stress, dim):
    Stress.sort(reverse=True)
    global sigma1, sigma2, sigma3
    sigma1=Stress[0]
    sigma2=Stress[1]
    center1_2=round((sigma1+sigma2)/2, 4)
    radius1_2=abs(sigma2-center1_2)

    if dim==3:
        sigma3=Stress[2]        
        center1_3=round((sigma1+sigma3)/2, 4)
        center2_3=round((sigma2+sigma3)/2, 4)    
        radius1_3=abs(sigma3-center1_3)    
        radius2_3=abs(sigma2-center2_3)
        
        print("The Principal Stresses are: \nσ1: {0} \nσ2: {1} \nσ3: {2} \n".format(sigma1,sigma2,sigma3))
        print("Maximum Shear Stress τ_max: " +str(round((sigma1-sigma3)/2, 3)))
        print("\nThe centers of the circle are: \nC1: {0} \nC2: {1} \nC3: {2} \n".format(center1_3,center1_2,center2_3))
    else:
        print("The Principal Stresses are: \nσ1: {0} \nσ2: {1} \n".format(sigma1,sigma2))
        print("Maximum Shear Stress τ_max: " +str(round((sigma1-sigma2)/2, 3))) 
        print("\nThe center of the circle are: \nC1: {0}".format(center1_2))           

    

    _, ax = plt.subplots()
    if dim == 3:
        ax.set(xlim=(center1_3-(radius1_3+0.5), sigma1+0.5), ylim = (-(radius1_3+1), radius1_3+1))
        mohr_center=[[center1_3,0],[center2_3,0],[center1_2,0]]
        mohr_sigma=[[sigma1,0],[sigma2,0],[sigma3,0]]
        ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
        ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
        for i in range(len(mohr_sigma)):
            ax.annotate("σ"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
        for i in range(len(mohr_center)):
            ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)

        Circle1_3 = plt.Circle((center1_3, 0),abs(radius1_3),fill=False, color="red")
        Circle2_3 = plt.Circle((center2_3, 0),abs(radius2_3),fill=False, color="blue")
        Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
        ax.add_artist(Circle1_3)
        ax.add_artist(Circle1_2)
        ax.add_artist(Circle2_3)
        ax.minorticks_on()
    elif dim ==2:
        ax.set(xlim=(center1_2-(radius1_2+0.5), sigma1+0.5), ylim = (-(radius1_2+0.5), radius1_2+0.5))
        mohr_center=[[center1_2,0]]
        mohr_sigma=[[sigma1,0],[sigma2,0]]
        ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
        ax.plot(*zip(*mohr_sigma), marker='o', color='b', ls='')
        for i in range(len(mohr_sigma)):
            ax.annotate("σ"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
        for i in range(len(mohr_center)):
            ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)
        Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
        ax.add_artist(Circle1_2)

    ax.minorticks_on()
    ax.set_aspect('equal', adjustable='box')
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.show()


def find_Principal_Stress(Stress_tensor):
    if Stress_tensor.shape == (3,3):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1] + a[2][2]
        I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
        I3 = np.linalg.det(Stress_tensor)
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        
        Plot_Mohr_Circle(list(a), dim=3)
    elif Stress_tensor.shape == (2,2):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1]
        print(a[0][1])
        I2= a[0][0]*a[1][1] - a[0][1]**2 
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        Plot_Mohr_Circle(list(a), dim=2)        

def input_to_tensor(σxx,σyy,σzz,σxy,σyz,σzx, n_dim):
    print()
    if n_dim==2:
        σ_tensor = [[σxx , σxy ],
                    [σxy , σyy ]]
    else:                    
        σ_tensor = [[σxx , σxy , σzx],
                    [σxy , σyy , σyz],
                    [σzx , σyz , σzz]]
    σ_tensor= np.array(σ_tensor)
    # print(σ_tensor.shape)
    find_Principal_Stress(σ_tensor)

def mohrCircle_execute(n_dim, input):
    if n_dim == 3:
        for i in range(3):
            if input[i+3]==None:
                input[i+3]=0

    input_to_tensor(σxx = input[0],σyy = input[1],σzz = input[3],σxy = input[2],σyz = input[4],σzx = input[5], n_dim=n_dim)

def sigma_1():
    global Stress_tensor
    if Stress_tensor.shape == (3,3):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1] + a[2][2]
        I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
        I3 = np.linalg.det(Stress_tensor)
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        return a[2]        
    elif Stress_tensor.shape == (2,2):
        a=Stress_tensor.copy()
        I1= a[0][0] + a[1][1]
        print(a[0][1])
        I2= a[0][0]*a[1][1] - a[0][1]**2 
        a=np.linalg.eig(a)[0]    
        a=np.round(a, 4)
        return a[1]

########### User input ##########
'''For two dimensional mohr circle, input only σxx,σyy,σxy, leave σzz,σyz,σzx as None'''
# σxx=1
# σyy=2
# σxy=1

# # '''For three dimensional mohr circle, input the following '''
# σzz=3
# σyz=0
# σzx=0
# input = [σxx, σyy, σxy, σzz, σyz, σzx]
# # ##################################

# mohrCircle_execute(n_dim=3,  input=input)

