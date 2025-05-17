# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:53:23 2023

@author: Michael
"""

def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1

array = [2, 4, 0, 1, 9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if (result == -1):
    print("No")
else:
    print("Element found: ", result)