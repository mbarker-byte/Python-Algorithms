# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:37:52 2023

@author: Michael
"""

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[minIndex] > arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        
        
array = [1, 4, 2, 10, 6, 5, 1]

selectionSort(array)
print(array)