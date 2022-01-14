"""
Some testing functions
"""
import matplotlib.pyplot as plt
import numpy as np


def add(var1,var2):
    "add"
    return var1+var2

def minus(var1,var2):
    "minus"
    return var1-var2

def multiple(var1,var2):
    "multiple"
    return var1*var2

def scatterplot():
    "scatterplot"
    x_list = np.linspace(0,2*np.pi,100)
    y_list = np.sin(x_list)
    plt.plot(x_list,y_list)
    plt.show()
    