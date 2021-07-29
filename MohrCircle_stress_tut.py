import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from MohrCircle_stress import Stress_MohrCircle
# reqAngle = 30
# isAngle = True

class tut_Stress_MohrCircle():
    def __init__(self, σxx,σyy,σxy,σzz = 0,σyz = 0,σzx = 0, angle1= None,angle2 = None,angle3 = None):
        self.σxx = σxx
        self.σyy = σyy
        self.σzz = σzz
        self.σxy = σxy
        self.σyz = σyz
        self.σzx = σzx
        self.angle2d = angle1
        self.angle1, self.angle2,  self.angle3 = angle1, angle2, angle3 
        # self.angle1, self.angle2, self.angle2 = np.cos(np.deg2rad(angle1)), np.cos(np.deg2rad(angle2)), np.cos(np.deg2rad(angle3))
        # self.angle3d = [np.cos(np.deg2rad(angle1)),np.cos(np.deg2rad(angle2)),np.cos(np.deg2rad(angle3))]
        self.ndims = 3
        self.is_centre = False
    
    def update_annot(self, point, idx):
        posx, posy = [point.get_xdata()[idx], point.get_ydata()[idx]]
        self.annot.xy = (posx, posy)
        text = f'({posx:.2f} , {posy:.2f})'
        self.annot.set_text(text)
        self.annot.get_bbox_patch().set_alpha(0.4)


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

    def annotate(self, points):
        self.pyg_pts = []
        for i in range(len(points)):
            l, = self.ax.plot(*zip(*points), marker='o', color='r', ls='')
            self.pyg_pts.append(l)


        self.annot = self.ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)
        self.figs.canvas.mpl_connect("motion_notify_event", self.hover)
        

    def _plot(self, ax):
            ax.minorticks_on()
            if(self.is_centre):
                ax.set_aspect('equal', adjustable='datalim')
            else:                
                ax.set_aspect('equal', adjustable='box')
            ax.spines['bottom'].set_position('center')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.grid(which='major', axis='both', linestyle ='--')
            plt.xlabel("σ Normal")
            plt.ylabel("σ Shear")
            self.annotate(self.annotate_pts)
            plt.show()
            self.is_centre = False
    def _calc_mohr(self):
        mohr_circle = Stress_MohrCircle(self.σxx, self.σyy,self.σxy, self.σzz,self.σyz,self.σzx)
        if(self.angle2d!=None and self.ndims==2):
            mohr_circle.isAngle_stress = True
            mohr_circle.reqAngle_stress_2d = self.angle2d
        elif(self.ndims==3 and self.angle1!=None and self.angle2!=None):
            l,m,n= np.cos(np.deg2rad(self.angle1)), np.cos(np.deg2rad(self.angle2)), np.cos(np.deg2rad(self.angle3))
            mohr_circle.isAngle_stress = True
            l,m,n = round(l,3),round(m,3),round(n,3)
            mohr_circle.reqAngle_normal_3d = list([l,m,n])
        mohr_circle.ndims = self.ndims
        return mohr_circle.stress_execute()

    def plot_cent(self):
        self.is_centre = True
        if(self.ndims == 2):
            self.mohr_cent,_,_,_,_,_ = self._calc_mohr()
            self.figs,self.ax = plt.subplots()
            for i in range(len(self.mohr_cent)):
                self.ax.annotate("C"+str(i+1),tuple(self.mohr_cent[i]),fontsize=12)
            self.init_pts = [[self.σxx, -self.σxy],[self.σyy,self.σxy]]
            self.ax.annotate('(σxx,-τxy)',tuple(self.init_pts[0]),fontsize = 12)
            self.ax.annotate('σyy,τxy)',tuple(self.init_pts[1]),fontsize = 12)
            self.ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            plt.xlabel("σ Normal")
            plt.ylabel("σ Shear")
            self.annotate_pts = self.mohr_cent+self.init_pts
            self._plot(self.ax)
        else:
            self.mohr_cent, self.mohr_sigma,_,_ = self._calc_mohr()
            self.figs,self.ax = plt.subplots()
            # self.ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            # self.ax.plot(*zip(*mohr_sigma), marker = 'o', color='b', ls='')

            for i in range(len(self.mohr_sigma)):
                self.ax.annotate("σ"+str(i+1),tuple(self.mohr_sigma[i]),fontsize=12)
            for i in range(len(self.mohr_cent)):
                self.ax.annotate("C"+str(i+1),tuple(self.mohr_cent[i]),fontsize=12)
            plt.xlabel("σ Normal")
            plt.ylabel("σ Shear")
            self.annotate_pts = self.mohr_cent+self.mohr_sigma

            self._plot(self.ax)

    def plot_init_pts(self):
        if(self.ndims)==2:
            self.is_centre = True
            self.figs,self.ax = plt.subplots()
            self.init_pts = [[self.σxx, -self.σxy],[self.σyy,self.σxy]]
            # for i in range(len(init_pts)):
            #     self.ax.annotate("σ"+str(i+1),tuple(init_pts[i]),fontsize=12)
            # self.ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            self.ax.annotate('(σxx,-τxy)',tuple(self.init_pts[0]),fontsize = 12)
            self.ax.annotate('σyy,τxy)',tuple(self.init_pts[1]),fontsize = 12)
            plt.xlabel("σ Normal")
            plt.ylabel("σ Shear")
            self.annotate_pts = self.init_pts
            self._plot(self.ax)

    def plot_circle(self):
        if(self.ndims==2):
            self.mohr_cent,self.mohr_sigma,radius,_,_,_ = self._calc_mohr()
            self.figs,self.ax = plt.subplots()
            self.ax.plot(*zip(*self.mohr_cent), marker='o', color='r', ls='')
            self.ax.plot(*zip(*self.mohr_sigma),marker='o', color='black', ls='')
            self.init_pts = [[self.σxx, -self.σxy],[self.σyy, self.σxy]]
            self.ax.annotate('(σxx,-τxy)',tuple(self.init_pts[0]),fontsize = 12)
            self.ax.annotate('σyy,τxy)',tuple(self.init_pts[1]),fontsize = 12)
            for i in range(len(self.mohr_sigma)):
                self.ax.annotate("σ"+str(i+1),tuple(self.mohr_sigma[i]),fontsize=12)
            for i in range(len(self.mohr_cent)):
                self.ax.annotate("C"+str(i+1),tuple(self.mohr_cent[i]),fontsize=12)
            # self.ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            self.ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            Circle1_2 = plt.Circle(tuple(self.mohr_cent[0]), abs(radius[0]), fill= False, color='green')
            self.ax.add_artist(Circle1_2)
            self.ax.set(xlim=((self.mohr_cent[0][0]-radius[0]-0.5), self.mohr_sigma[0][0]+0.5), ylim = (-(radius[0]+0.5), radius[0]+0.5))
            self.annotate_pts = self.mohr_cent + self.mohr_sigma + self.init_pts
            self._plot(self.ax)
    def plot_angle2d(self):
        if(self.ndims==2):
            mohr_cent,mohr_sigma,radius,new1,new2, curr_angle = self._calc_mohr()
            self.figs,self.ax = plt.subplots()
            fin_pts = [[new1[0],new1[1]],[new2[0],new2[1]]]
            self.ax.plot(*zip(*fin_pts), marker='o', color='orange', ls='')
            self.ax.plot([new1[0],new2[0]],[new1[1],new2[1]])
            # print(fin_pts)

            # self.ax.plot(*zip(*mohr_cent), marker='o', color='r', ls='')
            # self.ax.plot(*zip(*mohr_sigma),marker='o', color='black', ls='')
            init_pts = [[self.σxx, -self.σxy],[self.σyy,self.σxy]]
            self.ax.annotate('(σxx,-τxy)',tuple(init_pts[0]),fontsize = 12)
            self.ax.annotate('σyy,τxy)',tuple(init_pts[1]),fontsize = 12)
            for i in range(len(mohr_sigma)):
                self.ax.annotate("σ"+str(i+1),tuple(mohr_sigma[i]),fontsize=12)
            for i in range(len(mohr_cent)):
                self.ax.annotate("C"+str(i+1),tuple(mohr_cent[i]),fontsize=12)
            self.ax.annotate('(σ\'xx,-τ\'xy)',tuple(new1),fontsize = 12)
            self.ax.annotate('(σ\'yy, τ\'xy)',tuple(new2),fontsize = 12)
            # self.ax.plot(*zip(init_pts), marker = 'o', color='b', ls='')
            self.ax.plot([self.σxx,self.σyy],[-self.σxy,self.σxy])
            Circle1_2 = plt.Circle(tuple(mohr_cent[0]), abs(radius[0]), fill= False, color='green')
            self.ax.add_artist(Circle1_2)
            self.ax.set(xlim=((mohr_cent[0][0]-radius[0]-0.5), mohr_sigma[0][0]+0.5), ylim = (-(radius[0]+0.5), radius[0]+0.5))
            self.annotate_pts = mohr_cent + mohr_sigma + [new1,new2] + init_pts
            self._plot(self.ax)
    def get_I_values(self):
        a  = [[self.σxx , self.σxy , self.σzx],
              [self.σxy , self.σyy , self.σyz],
              [self.σzx , self.σyz , self.σzz]]
        I1 = a[0][0] + a[1][1] + a[2][2]
        i2 = a[0][0]*a[1][1] + a[1][1]*a[2][2] + a[0][0]*a[2][2] - a[0][1]**2 - a[0][2]**2 -a[1][2]**2
        I3 = np.linalg.det(a)
        return I1,i2,I3
    def get_princip_values(self):
        a  = [[self.σxx , self.σxy , self.σzx],
              [self.σxy , self.σyy , self.σyz],
              [self.σzx , self.σyz , self.σzz]]
        a = np.linalg.eig(a)[0]
        a = np.round(a, 4)
        return a
    def plot_circle_3d(self):
        mohr_circle = Stress_MohrCircle(self.σxx, self.σyy,self.σxy, self.σzz,self.σyz,self.σzx)
        mohr_circle.isGraph = True
        mohr_circle.stress_execute()
# m = tut_Stress_MohrCircle(1,2,3,4,5,6)
# m.ndims = 2
# m.angle2d = 30
# # m.plot_circle_3d()
# m.plot_circle()
# m.plot_cent()
# m.plot_angle2d()
# m.plot_init_pts()
# m.ndims = 3
# m.plot_circle_3d()
