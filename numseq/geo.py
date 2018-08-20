'''
Module for getting values in a geometric sequence e.g. square, triangle, cube
'''


def square(n):
    '''returns nth number in square geometric sequence'''
    return n**2


def triangle(n):
    '''returns nth number in triangle geometric sequence'''
    if n is 0:
        return 0
    a, b = 1, 3
    inc_val = 3
    my_list = []
    for i in range(n):
        my_list.append(a)
        a, b = b, b + inc_val
        inc_val += 1
    return my_list[-1]


def cube(n):
    '''returns nth number in cube geometric sequence'''
    return n**3
