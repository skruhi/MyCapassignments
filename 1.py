# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:19:06 2022

@author: skruh
"""
from math import pi

radius = float(input('enter the radius of the circle:'))
area = pi *radius*radius
print("area of the circle is : {0}". format(area))

filename = input( "input filename:")
f_extns=filename.split(".")

print("extension of file is:" (f_extns[-1]))