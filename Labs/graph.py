import matplotlib.pyplot as plt
import numpy as np


class Graph:

    def f(x):
        return x

    def __init__(self, function= lambda x: x, end_points=10,step_size = 1):
        self.end_points = end_points
        self.function = function
        self.step_size = step_size

    def plot(self,fname="Figure"):
        # counter = 0
        xval = []
        xtemp = 0
        yval = []
        while xtemp < self.end_points:
            yval.append(self.function(xtemp))
            xval.append(xtemp)
            xtemp += self.step_size

        plt.plot(xval,yval)
        fig = plt.gcf()
        # plt.show()

        fig.savefig("%s.png" %fname)
