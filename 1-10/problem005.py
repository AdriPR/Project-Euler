#
# Project Euler Solution
# Problem ID: 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#

# The fastest way to calculate it is using lcm method from math library
#
# import math
#
# def is_divisible():
#     n = math.lcm(11,12,13,14,15,16,17,18,19,20)
#     return print(f'The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {n}')

def is_divisible():
    n = 60

    while True:
        found = True
        i = 11
        while i<=20 and found:
            found = found and n % i == 0
            i = i + 1
        if found: 
            return print(f'The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: {n}')
        else:
            n = n + 60

if __name__ == '__main__':
    is_divisible()