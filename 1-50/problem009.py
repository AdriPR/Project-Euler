#
# Project Euler Solution
# Problem ID: 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a^2 + b^2 = c^2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

import math

def triplet():
    for n in range(1, 100):
        for m in range(n, 100):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if a + b + c == 1000:
                return print(f'Solution: {math.prod([a, b, c])}')

if __name__ == '__main__':
    triplet()