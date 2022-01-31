# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 23:06:53 2022

@author: skruh
"""
str= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] -= 1
    return d

print (most_frequent(str))