"""
Some testing functions
"""
import matplotlib.pyplot as plt
import numpy as np


def add(a,b):
    return a+b

def minus(a,b):
    return a-b

def multiple(a,b):
    return a*b

def scatterplot():
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    plt.plot(x,y)
    plt.show()
    