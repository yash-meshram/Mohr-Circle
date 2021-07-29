import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)

points = [[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]]
fig, ax = plt.subplots()
pyg_pts = []
for i in range(len(points)):
    l, = ax.plot(*zip(*points), marker='o', color='r', ls='')
    pyg_pts.append(l)


annot = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)


def update_annot(line, idx):
    posx, posy = [line.get_xdata()[idx], line.get_ydata()[idx]]
    annot.xy = (posx, posy)
    text = f'{posx:.2f}-{posy:.2f}'
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)


def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for point in pyg_pts:
            cont, ind = point.contains(event)
            if cont:
                update_annot(point, ind['ind'][0])
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()


fig.canvas.mpl_connect("motion_notify_event", hover)
plt.show()