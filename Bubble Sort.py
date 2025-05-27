# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:16:18 2023

@author: Michael
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range (n-1):
        swapped = False
        for j in range (0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped == False:
            break
            
array =[1, 12, 11, 10, 4, 5]

bubbleSort(array)

print(array)