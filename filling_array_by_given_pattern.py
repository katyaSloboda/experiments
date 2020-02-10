# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 03:25:13 2019
"""

import random


def fill_map_with_rhombus(custom_map, mh, mw, ki, kj, i, j, nextNum):
    """Filling map according to the given picture (rhombus).
    Input arguments:
        custom_map - an initial map,
        mh - map height,
        mw - map width,
        ki - vertical direction (-1 - up, 1 - down, 0 - stay in place),
        kj - horizontal direction (-1 - left, 1 - right, 0 - stay in place),
        i and j - cell coordinates to fill (row and column)
        nextNum - next number for empty cell.
    The function returns None (default), modifies the input array (custom_map).
    
    """
    # if i or j out of range
    if i < 0 or j < 0 or i >= mh or j >= mw:
        # up
        if ki == -1 and kj == 0:
            i += mh; j = (j + 1) % mw
        # right
        elif ki == 0 and kj == 1:
            i = (i + 1) % mh; j = 0
        # down
        elif ki == 1 and kj == 0:
            i = 0; j = (j + 1) % mw
        # left
        elif ki == 0 and kj == -1:
            i = (i + 1) % mh; j += mw
        
        # up and left
        elif ki == -1 and kj == -1:
            if i == -1 and j == mw - 2:
                i = mh - 1; j = 0
            else:
                r = min(mh - 1 - i, mw - 1 - j)
                i += r; j += r
                if j < mw - 1:
                    j += 1
                else:
                    i -= 1
                    
        # up and right
        elif ki == -1 and kj == 1:
            if i == -1 and j == 1:
                i = mh - 1; j = mw - 1
            else:
                r = min(mh - 1 - i, j)
                i += r; j -= r
                if j > 0:
                    j -= 1
                else:
                    i -= 1
                    
        # down and right
        elif ki == 1 and kj == 1:
            if i == mh and j == 1:
                i = 0; j = mw - 1
            else:
                r = min(i, j)
                i -= r; j -= r
                if j > 0:
                    j -= 1
                else:
                    i += 1
                    
        # down and left
        elif ki == 1 and kj == -1:
            if i == mh and j == mw - 2:
                i = 0; j = 0
            else:
                r = min(i, mw - 1 - j)
                i -= r; j += r
                if j < mw - 1:
                    j += 1
                else:
                    i += 1
            
        fill_map_with_rhombus(custom_map, mh, mw, ki, kj, i, j, nextNum)
        
    else:
        # changing direction
        if custom_map[i][j] == 0:
            ki = random.randrange(-1, 2, 1)
            kj = random.randrange(-1, 2, 1)
        
        # filling empty cell
        elif custom_map[i][j] == -1:
            custom_map[i][j] = nextNum
            nextNum += 1
            if nextNum > mh * mw - 4:
                return
            
        fill_map_with_rhombus(custom_map, mh, mw, ki, kj, i + ki, j + kj, nextNum)


def get_map_with_rhombus(mh, mw, rh, rw):
    """Function for building a custom map using a rhombus.
    Input arguments:
        mh - map height,
        mw - map width,
        rh - rhombus height,
        rw - rhombus width.
    Returns a map (an array of numbers) that is filled according to the given 
    picture.
    
    """
    if (mh < 3 or mw < 3 or rh < 3 or rw < 3 or mh < rh or mw < rw):
        print('The minimum dimensions of the map and rhombus must be 3 by 3. ',
              'Map size must be larger than rhombus size.')
        return []
    
    hmh, hmw, hrh, hrw = mh // 2, mw // 2, rh // 2, rw // 2
    
    # Creating an initial map
    custom_map = [[0 if i == hmh and
                        (j == hmw - hrw or j == hmw + hrw + rw % 2 - 1) or 
                        j == hmw and
                        (i == hmh - hrh or i == hmh + hrh + rh % 2 - 1)
                   else -1 for j in range(mw)] for i in range(mh)]
    
    # Filling map according to the given picture
    fill_map_with_rhombus(custom_map, mh, mw, 0, 1, 0, 0, 1)
    return custom_map


print(get_map_with_rhombus(3,3,3,3))
print(get_map_with_rhombus(4,4,4,4))
print(get_map_with_rhombus(4,3,3,3))
print(get_map_with_rhombus(3,4,3,3))
print(get_map_with_rhombus(5,5,4,4))
print(get_map_with_rhombus(20,20,4,4))




















