#!/usr/bin/env python3 
'''
    A function that returns a list of list of intergers representing the Pascal Triangle
'''
def pascal_triangle(n):
    #note n is the number of row
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle