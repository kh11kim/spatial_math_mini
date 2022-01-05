import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# axeslength = 1
# axeswidth = 5
# dims = None
# fig = None
# ax = None
# def plot(self, **kwargs):
#     """[summary]
#     """
#     if self.fig is None:
#         raise Exception("plot_init first")
#     frame_plot(self.R, self.p, self.ax, base.scale,
#                 axeslength=self.axeslength,
#                 axeswidth=self.axeswidth,
#                 **kwargs)

# def plot_init(self, dims=None):
#     if dims is None:
#         raise Exception("dims are needed!")        
#     base.dims = dims
#     base.scale = dims[1]-dims[0]
#     base.fig = plt.figure()
#     base.ax = plt.axes(projection='3d')
#     base.ax = plot3d_init(base.ax, base.dims)
#     self.plot_frame_0()

# def plot_clear(self):
#     base.ax.clear()
#     base.ax = plot3d_init(base.ax, base.dims)
#     self.plot_frame_0()

# def plot_frame_0(self):
#     frame_plot(np.eye(3), np.zeros(3), self.ax, base.scale,
#                 color='k',
#                 axeslength=self.axeslength,
#                 axeswidth=self.axeswidth)

def frame_plot(R, p, ax, scale, frame=None, color=None, axeslength=1, axeswidth=5):
    """[summary]
    Draw Frame by R, p

    Args:
        R (3x3 np.ndarray): Rotation Matrix
        p (size 3 np.ndarray): Translation vector
        frame ('str', optional): the name of a frame. Defaults to None.
        dims (size 6 np.ndarray or list, optional): 
            view scope limit. Defaults to [0,10]*3.
        axeslength (int, optional): [description]. Defaults to 1.
        axeswidth (int, optional): [description]. Defaults to 5.
    """
    if color is None:
        if frame is None:
            colors = ['gray']*3
        else:
            colors = ['r','g','b']
    else:
        colors = color*3

    for i in range(3):
        axis = np.vstack([p, p+R[:3,i]*axeslength]).T 
        ax.plot(axis[0], axis[1], axis[2], 
            color=colors[i], linewidth=axeswidth)

    frame_name_offset = [-0.01, -0.01, -0.01]
    frame_name_pos = R.dot(scale*np.array(frame_name_offset).T)+p
    if frame is not None:
        ax.text(*frame_name_pos, "{{{}}}".format(frame))

def plot3d_init(ax, dims):
    ax.set_xlim3d(dims[:2])
    ax.set_ylim3d(dims[2:4])
    ax.set_zlim3d(dims[4:])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    return ax

# # Check if there is a 3d figure
# is_3d_plot = False
# if len(plt.get_fignums()) != 0:
#     fig = plt.gcf()
#     if len(fig.axes) != 0:
#         ax = plt.gca()
#         if ax.__class__.__name__ == "Axes3DSubplot":
#             is_3d_plot = True

# # if there is no 3d figure, make one.
# if not is_3d_plot:
#     plot3d_init(dims)