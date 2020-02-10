# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:43:09 2019
"""

import random
from functools import cmp_to_key


def bit_comp(x, y):
    """Pattern for sorting bits.
    Input arguments:
        x, y - bits that are compared.
    Returns: -1 if x < y,
              0 if x == y,
              1 if x > y
    
    """
    if (int(x[6]) != int(y[6])):
        return int(y[6]) - int(x[6])
    elif (int(x[2]) != int(y[2])):
        return int(x[2]) - int(y[2])
    elif (int(x[0]) != int(y[0])):
        return int(y[0]) - int(x[0])
    elif (int(x[3]) != int(y[3])):
        return int(x[3]) - int(y[3])
    elif (int(x[1]) != int(y[1])):
        return int(y[1]) - int(x[1])
    elif (int(x[5]) != int(y[5])):
        return int(x[5]) - int(y[5])
    elif (int(x[4]) != int(y[4])):
        return int(x[4]) - int(y[4])
    else:
        return int(x[7]) - int(y[7])
    
    
def custom_sorted(arr, comp_func):
    """Function for sorting numbers by a given pattern.
    Input arguments:
        arr - list which should be sorted,
        comp_func - function that contains the sort pattern.
    Returns a sorted list
    
    """
    for n in range(1, len(arr)):
       for i in range(len(arr) - n):
           if comp_func(arr[i], arr[i + 1]) > 0 :
               arr[i], arr[i + 1] = arr[i + 1], arr[i]       
    return arr


# Creating random list
arr = [format(random.getrandbits(8), "b") for i in range(7)]

# Adding zeros to array elements for a length of 8 characters
arr = ['0' * (8 - len(i)) + i for i in arr]
print('arr: ', arr, '\n')

arr1 = sorted(arr, key=cmp_to_key(bit_comp))
print('arr1:')
for i in arr1:
    print(i[::-1])

arr2 = custom_sorted(arr, bit_comp)
print('\narr2:')
for i in arr2:
    print(i[::-1])


























