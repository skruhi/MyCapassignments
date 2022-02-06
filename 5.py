# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:19:06 2022

@author: skruh
"""
import math 

radius = float(input('enter the radius of the circle:'))
area = math.pi *radius*radius
print("area of the circle is : {0}". format(area))

filename = input( "input filename:")
f = filename.split(".")
print("extension of file is:" + (f[-1]))