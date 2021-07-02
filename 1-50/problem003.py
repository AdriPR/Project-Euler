#
# Project Euler Solution
# Problem ID: 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#

import math

def is_prime(n):
    return not any(i for i in range(2, int(math.sqrt(n)+1.0)) if n%i == 0)

def largest_prime(n):
    i = 2
    while n != 1:
        if is_prime(i) and n%i == 0:
            res = i
            n = n / i
            continue
        else:
            i = i + 1
            
    return print(f'The largest prime factor of the number 600851475143 is: {res}')

if __name__ == '__main__':
    largest_prime(600851475143)