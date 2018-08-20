'''
Module for getting a list of prime numbers & checking whether a number is prime
'''


def primes(n):
    '''primes(n) returns a list of all primes less than n'''
    my_list = []
    for num in range(2, n):
        if all(num % i != 0 for i in range(2, num)):
            my_list.append(num)
    return my_list


def is_prime(m):
    '''is_prime(m) returns a boolean indicating whether m is a prime number'''
    m = abs(int(m))
    if m < 2:
        return False
    if m == 2:
        return True
    if not m & 1:
        return False
    for i in range(3, int(m**0.5) + 1, 2):
        if m % i == 0:
            return False
    return True
