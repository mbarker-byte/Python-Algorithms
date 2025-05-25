# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:12:47 2023

@author: Michael
"""

            

def mergeSort(array):
     if len(array) > 1:
         mid = len(array) // 2
         left = array[:mid]
         right = array [mid:]
         
         mergeSort (left)
         mergeSort(right)
         merge(array, left, right)
         
def merge(array, left, right):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i =+ 1
        k =+ 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
         
arr = [14,46,15,32,12,27,16,67,57,41,42,43,1000,7,19,47,9,112]

mergeSort(arr)
print(arr)
print("q")