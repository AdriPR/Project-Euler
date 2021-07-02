#
# Project Euler Solution
# Problem ID: 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#

import math

def is_prime(n):
    return not any(i for i in range(2, int(math.sqrt(n)+1.0)) if n%i == 0)

def sum_primes(n):
    l = [i for i in range(2, n) if is_prime(i)]       
    return print(f'Solution: {sum(l)}')

if __name__ == '__main__':
    sum_primes(2000000)