# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 20:20:42 2022

@author: skruh
"""

from collections import Counter
s = input()
d = dict(Counter(s))
def get_key(val):
    for key, value in d.items():
        if val == value:
            return key
for i in sorted(d.values(), reverse = True):
    print(get_key(i), "=", i)
    
    
    
    
    
    
    