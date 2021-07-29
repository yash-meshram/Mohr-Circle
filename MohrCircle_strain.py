# Rwik - IIT Gn
# Code for Strains in Mohr Circle
import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

# Each calculation can be put into the following class:
class Strain_MohrCircle():
    def __init__(self, εxx,εyy,εxy,εzz = 0,εyz = 0,εzx = 0):
        self.εxx = εxx
        self.εyy = εyy
        self.εzz = εzz
        self.εxy = εxy
        self.εyz = εyz
        self.εzx = εzx
        self.ndims = 3 #by default each object of class has property of 3-D Mohr-Circle
        self.isGraph = False
        self.isAngle_strain = False #To be made True if angle of a plane is given
        self.reqAngle_strain_2d = None #the required angle for 2_D mohr (in degrees)
        self.reqAngle_normal_3d = [0,0,0] #required angle for 3-D mohr (cosine values of the angles)
    
    def update_annot(self, point, idx):
        posx, posy = [point.get_xdata()[idx], point.get_ydata()[idx]]
        self.annot.xy = (posx, posy)
        text = f'({posx:.2f} , {posy:.2f})'
        self.annot.set_text(text)
        self.annot.get_bbox_patch().set_alpha(0.4)

    # The following two functions update_annot and hover are utiltity 
    # functions for annotation on the points plotted via matplotlib
    def hover(self, event):
        vis = self.annot.get_visible()
        if event.inaxes == self.ax:
            for point in self.pyg_pts:
                cont, ind = point.contains(event)
                if cont:
                    self.update_annot(point, ind['ind'][0])
                    self.annot.set_visible(True)
                    self.figs.canvas.draw_idle()
                else:
                    if vis:
                        self.annot.set_visible(False)
                        self.figs.canvas.draw_idle()

    # Calculating and plotting the Mohr_Circle
    def Find_Mohr_Circle(self):
        Strain = list(self.principal_strain)
        Strain_tensor = self.ε_tensor
        # Sorting the values of eigen values in the form of epsi1>epsi2>epsi3
        Strain.sort(reverse=True)
        epsi1=Strain[0]
        epsi2=Strain[1]
        center1_2=round((epsi1+epsi2)/2, 4)
        radius1_2=abs(epsi2-center1_2)
        # Additional params for 3-D strain
        if self.ndims==3:
            epsi3=Strain[2]        
            center1_3=round((epsi1+epsi3)/2, 4)
            center2_3=round((epsi2+epsi3)/2, 4)    
            radius1_3=abs(epsi3-center1_3)    
            radius2_3=abs(epsi2-center2_3)
            # Printing the outputs in the command prompt
            print("The Principal Straines are: \nε1: {0} \nε2: {1} \nε3: {2} \n".format(epsi1,epsi2,epsi3))
            print("Maximum Shear Strain epsi_max: " +str(round((epsi1-epsi3)/2, 3)))
            print("\nThe centers of the circle are: \nC1: {0} \nC2: {1} \nC3: {2} \n".format(center1_3,center1_2,center2_3))
        else:
            print("The Principal Straines are: \nε1: {0} \nε2: {1} \n".format(epsi1,epsi2))
            print("Maximum Shear Strain epsi_max: " +str(round((epsi1-epsi2)/2, 3))) 
            print("\nThe center of the circle are: \nC1: {0}".format(center1_2))           

        
        new_x_1, new_x_2,new_y_1,new_y_2 = None, None, None, None
        epsi_NN,epsi_NS, princip_angle = None, None, None
        radius = []
        self.ax = None
        if self.isGraph:
            self.figs, self.ax = plt.subplots()
        if self.ndims == 3:
            radius = [radius1_2,radius2_3,radius1_3]
            mohr_center=[[center1_3,0],[center2_3,0],[center1_2,0]]
            mohr_epsi=[[epsi1,0],[epsi2,0],[epsi3,0]]
            if(self.isAngle_strain):
                l = self.reqAngle_normal_3d[0]
                m = self.reqAngle_normal_3d[1]
                n2 = 1 - l**2 - m**2
                print(l,m,n2)
                if(n2<0):
                    print("Invalid Angle input!!!!!")
                    raise ValueError('Bad input!')
                # else:
                n = np.sqrt(n2)
                epsi_NN = (l**2)*epsi1 + (m**2)*epsi2 + (n**2)*epsi3
                epsi_NS = np.sqrt((l**2)*epsi1**2 + (m**2)*epsi2**2 + (n**2)*epsi3**2 - epsi_NN**2)
            if(self.isGraph):
                self.ax.set(xlim=(center1_3-(radius1_3+0.5), epsi1+0.5), ylim = (-(radius1_3+1), radius1_3+1))
                self.ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
                self.ax.plot(*zip(*mohr_epsi), marker='o', color='b', ls='')
                for i in range(len(mohr_epsi)):
                    self.ax.annotate("ε"+str(i+1),tuple(mohr_epsi[i]),fontsize=12)
                for i in range(len(mohr_center)):
                    self.ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)

                Circle1_3 = plt.Circle((center1_3, 0),abs(radius1_3),fill=False, color="red")
                Circle2_3 = plt.Circle((center2_3, 0),abs(radius2_3),fill=False, color="blue")
                Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
                print(self.isAngle_strain)
                if(self.isAngle_strain):
                    new_points = [[epsi_NN,epsi_NS]]
                    print(new_points)
                    self.ax.plot(*zip(*new_points),marker='o', color='purple', ls='')
                    # n = self.reqAngle_normal_3d[2]
                self.ax.add_artist(Circle1_3)
                self.ax.add_artist(Circle1_2)
                self.ax.add_artist(Circle2_3)
                self.ax.minorticks_on()
        elif self.ndims ==2:
            radius = [radius1_2]
            mohr_center=[[center1_2,0]]
            mohr_epsi=[[epsi1,0],[epsi2,0]]
            try:
                curr_angle = np.arctan((Strain_tensor[0][1])/(Strain_tensor[0][0]-center1_2))
                princip_angle = np.arctan(-(Strain_tensor[0][1])/(-Strain_tensor[0][0] +center1_2))/2
            except:
                if(Strain_tensor[0][1]>=0):
                    curr_angle = np.deg2rad(90)
                    princip_angle = np.arctan(-(Strain_tensor[0][1])/(Strain_tensor[0][0]-center1_2))/2

                else:
                    curr_angle = np.deg2rad(-90)
                    princip_angle = np.arctan(-(Strain_tensor[0][1])/(Strain_tensor[0][0]-center1_2))/2

            if(self.isAngle_strain):
                
                total_angle = np.deg2rad(2*self.reqAngle_strain_2d)
                new_x_1 = (Strain_tensor[0][0] + Strain_tensor[1][1])/2 + np.cos(total_angle)*(Strain_tensor[0][0] - Strain_tensor[1][1])/2 + Strain_tensor[0][1] * np.sin(total_angle)
                new_y_1 = -(-np.sin(total_angle)*(Strain_tensor[0][0] - Strain_tensor[1][1]) + 2*Strain_tensor[0][1] * np.cos(total_angle))/2
                new_x_2 = (Strain_tensor[0][0] + Strain_tensor[1][1])/2 - np.cos(total_angle)*(Strain_tensor[0][0] - Strain_tensor[1][1])/2 - Strain_tensor[0][1] * np.sin(total_angle)
                new_y_2 = -new_y_1
            
            
            if(self.isGraph):
                self.ax.set(xlim=(center1_2-(radius1_2+0.5), epsi1+0.5), ylim = (-(radius1_2+0.5), radius1_2+0.5))
                self.ax.plot(*zip(*mohr_center), marker='o', color='r', ls='')
                self.ax.plot(*zip(*mohr_epsi), marker='o', color='b', ls='')
                initial_pts = [[Strain_tensor[0][0],-Strain_tensor[0][1]],[Strain_tensor[1][1],Strain_tensor[0][1]]]
                self.ax.plot(*zip(*initial_pts),marker='o', color='black', ls='')
                self.ax.plot([Strain_tensor[0][0],Strain_tensor[1][1]],[-Strain_tensor[0][1],Strain_tensor[0][1]])
                self.ax.annotate("(εxx ,-γxy/2)",tuple([Strain_tensor[0][0], - Strain_tensor[0][1]]),fontsize = 12)
                self.ax.annotate("(εyy , γxy/2)",tuple([Strain_tensor[1][1],   Strain_tensor[0][1]]),fontsize = 12)
                if(self.isAngle_strain):
                    new_points = [[new_x_1,new_y_1],[new_x_2,new_y_2]]
                    self.ax.annotate('(ε\'xx,-γ\'xy/2)',tuple(new_points[0]),fontsize = 12)
                    self.ax.annotate('(ε\'yy,γ\'xy/2)',tuple(new_points[1]),fontsize = 12)
                    self.ax.plot(*zip(*new_points),marker='o', color='black', ls='')
                    self.ax.plot([new_x_1,new_x_2],[new_y_1,new_y_2])
                for i in range(len(mohr_epsi)):
                    self.ax.annotate("ε"+str(i+1),tuple(mohr_epsi[i]),fontsize=12)
                for i in range(len(mohr_center)):
                    self.ax.annotate("C"+str(i+1),tuple(mohr_center[i]),fontsize=12)
                Circle1_2 = plt.Circle((center1_2, 0),abs(radius1_2),fill=False, color="green")
                self.ax.add_artist(Circle1_2)
        # Plotting
        if(self.isGraph):
            if self.ndims==2:
                points = mohr_center+mohr_epsi+[[new_x_1,new_y_1],[new_x_2,new_y_2]]+initial_pts
            else:
                points = mohr_center+mohr_epsi+[[epsi_NN,epsi_NS]]

            self.pyg_pts = []
            for i in range(len(points)):
                l, = self.ax.plot(*zip(*points), marker='o', color='r', ls='')
                self.pyg_pts.append(l)


            self.annot = self.ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                bbox=dict(boxstyle="round", fc="w"),
                                arrowprops=dict(arrowstyle="->"))
            self.annot.set_visible(False)
            self.figs.canvas.mpl_connect("motion_notify_event", self.hover)

            self.ax.minorticks_on()
            self.ax.set_aspect('equal', adjustable='box')

            self.ax.spines['bottom'].set_position('center')
            self.ax.xaxis.set_ticks_position('bottom')
            self.ax.yaxis.set_ticks_position('left')
            self.ax.grid(which='major', axis='both', linestyle ='--')
            plt.xlabel("ε Normal")
            plt.ylabel("γ/2 Shear")
            plt.show()
            plt.close('all')

        if(self.ndims == 2):
            return mohr_center, mohr_epsi, radius ,(new_x_1, new_y_1), (new_x_2, new_y_2), princip_angle
        else:
            return mohr_center, mohr_epsi, radius ,(epsi_NN, epsi_NS)

    # Finding the principal straines using eigen values ONLY
    def find_Principal_Strain(self):
        if self.ε_tensor.shape == (3,3):
            a=self.ε_tensor.copy()
            '''The following code is only for reference'''
            # self.I1= a[0][0] + a[1][1] + a[2][2]
            # self.I2= a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
            # self.I3 = np.linalg.det(self.ε_tensor)
            a=np.linalg.eig(a)[0]                
            self.principal_strain=np.round(a, 4)
            return Strain_MohrCircle.Find_Mohr_Circle(self)
        elif self.ε_tensor.shape == (2,2):
            a=self.ε_tensor.copy()
            self.I1= a[0][0] + a[1][1]
            self.I2= a[0][0]*a[1][1] - a[0][1]**2 
            a=np.linalg.eig(a)[0]    
            self.principal_strain=np.round(a, 4)
            return Strain_MohrCircle.Find_Mohr_Circle(self)        
    # Main executable

    def strain_execute(self):
        if self.ndims==2:
            self.ε_tensor = [[self.εxx , self.εxy/2 ],
                        [self.εxy/2 , self.εyy ]]
        else:                    
            self.ε_tensor = [[self.εxx , self.εxy/2 , self.εzx/2],
                        [self.εxy/2 , self.εyy , self.εyz/2],
                        [self.εzx/2 , self.εyz/2 , self.εzz]]
        self.ε_tensor= np.array(self.ε_tensor)
        # print(ε_tensor.shape)
        return Strain_MohrCircle.find_Principal_Strain(self)

# uncomment the code for executing this file separately
# Don't foget to comment it back before using the Pygame app
'''Examples'''
'''3-D'''
'''m is an object of class Strain_MohrCircle'''
# m = Strain_MohrCircle(σxx= 34.3, σyy= 74,σzz= 3, σxy= -83.9, σyz= 5, σzx= 6)
# m.ndims = 3
# m.isGraph = True
# m.isAngle_Strain = True
# m.reqAngle_normal_3d = [round(np.cos(np.deg2rad(30)),3), round(np.cos(np.deg2rad(60)),3), np.cos(90)]
# '''Note that the last value of angle is a dummy value'''
# m.Strain_execute()


'''2-D'''
# m = Strain_MohrCircle(σxx= 34.3, σyy= 74,σzz= 3, σxy= -83.9, σyz= 5, σzx= 6)
# m.ndims = 2
# m.isGraph = True
# m.isAngle_strain = True
# m.reqAngle_strain_2d = 54.6
# m.strain_execute()

