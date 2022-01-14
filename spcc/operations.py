"""
Some testing functions
"""
import matplotlib.pyplot as plt
import numpy as np


def add(aa,bb):
    "add"
    return aa+bb

def minus(aa,bb):
    "minus"
    return aa-bb

def multiple(aa,bb):
    "multiple"
    return aa*bb

def scatterplot():
    "scatterplot"
    x_list = np.linspace(0,2*np.pi,100)
    y_list = np.sin(x_list)
    plt.plot(x_list,y_list)
    plt.show()
    