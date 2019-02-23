import sys
import random
import pandas as pd
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker, cm
import json
import noise
import math
import numpy as np


class NeurocadWidgets(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        lay = QtWidgets.QVBoxLayout(self)
        lay.addWidget(self.canvas)
        self.update_gaussian()
        self.update_perlin()
        self.update_graph()

    def update_gaussian(self):
        noise, gaussian, blend = mathematical_derivation()
        print(gaussian)
        fig, ax = plt.subplots()
        ax = self.canvas.figure.add_subplot(111)
        ax.imshow(gaussian, cmap=cm.gist_gray)
        self.canvas.draw()

    def update_perlin(self):
        noise, gaussian, blend = mathematical_derivation()
        fig, ax = plt.subplots()
        ax = self.canvas.figure.add_subplot(111)
        ax.imshow(noise, cmap=cm.gist_gray)
        self.canvas.draw()

    def update_graph(self):
        noise, gaussian, blend = mathematical_derivation()
        fig, ax = plt.subplots()
        ax = self.canvas.figure.add_subplot(111)
        ax.imshow(blend, cmap=cm.gist_gray)
        self.canvas.draw()


def mathematical_derivation():
    shape = (500, 500)
    scale_x = 50.0
    scale_y = 50.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    data = json.loads(open('list_perlin_value.json').read())
    scale_x = data[0]
    scale_y = data[1]
    lineContrast = data[2]

    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i / scale_x,
                                        j / scale_y,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=int(lineContrast))

    data = json.loads(open('list_gaussian_value.json').read())
    print(data[1])
    center_x, center_y = shape[1] // 2, shape[0] // 2
    circle_grad = np.zeros_like(world)

    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            distx = abs(x - center_x)
            disty = abs(y - center_y)
            dist = math.sqrt(distx*distx + disty*disty)
            circle_grad[y][x] = dist

    # get it between -1 and 1
    max_grad = np.max(circle_grad)
    circle_grad = circle_grad / max_grad
    circle_grad -= data[1]
    circle_grad *= 2.0
    circle_grad = -circle_grad

    # shrink gradient
    for y in range(world.shape[0]):
        for x in range(world.shape[1]):
            if circle_grad[y][x] > 0:
                circle_grad[y][x] *= 20

    # get it between 0 and 1
    max_grad = np.max(circle_grad)
    circle_grad = circle_grad / max_grad


    world_noise = np.zeros_like(world)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world_noise[i][j] = (world[i][j] * circle_grad[i][j])
            if world_noise[i][j] > 0:
                world_noise[i][j] *= 20

    # get it between 0 and 1
    max_grad = np.max(world_noise)
    world_noise = world_noise / max_grad

    return world,circle_grad,world_noise
#
# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     w = NeurocadWidgets()
#     w.show()
#     sys.exit(app.exec_())

