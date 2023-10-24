# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 16:51:40 2023

@author: trevb
"""

import pandas as pd
import numpy as np

def mandelbrot(x, y, x0, y0, depth, max_depth):
    if((x**2 + y**2 > 2) or (depth >= max_depth)):
        return depth
    else:
        x_new = x**2 - y**2 + x0
        y_new = 2*x*y + y0
        return mandelbrot(x_new, y_new, x0, y0, depth + 1, max_depth)

def calculate(xrange, yrange, resolution, depth):
    x = np.linspace(xrange[0], xrange[1], resolution)
    y = np.linspace(yrange[0], yrange[1], resolution)
    
    results = np.zeros((resolution,resolution))
    for i in range(resolution):
        for j in range(resolution):
            results[i,j] = mandelbrot(x[i],y[j],x[i],y[j],0,depth)

    return results, x, y

if __name__ == '__main__':
    
    x = np.linspace(-2,2,200)
    y = np.linspace(-2,2,200)
    
    results = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            results[i,j] = mandelbrot(x[i],y[j],x[i],y[j],0,20)
        print(i)