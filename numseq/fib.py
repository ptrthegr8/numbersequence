'''
Module for getting a number in the Fibonacci Sequence.
'''


def fib(n):
    '''Given n, returns the nth Fibonacci number.'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b - a
