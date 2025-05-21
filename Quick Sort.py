# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:41:18 2023

@author: Michael
"""

def quickSort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)
        #

def partition(start, end, array):
    pivotIndex = start
    pivot = array[pivotIndex]
    
    while start < end:
        
        while start < len(array) and array[start] <= pivot:
            start += 1
            
        while array[end] > pivot:
            end -= 1
            
        if (start < end):
            array[start], array[end] = array[end], array[start]
    
    array[end], array[pivotIndex] = array[pivotIndex], array[end]
    
    return end

arr = [10,12,4,6,56,14,98,112]
quickSort(0, len(arr) -1, arr)

print(arr)