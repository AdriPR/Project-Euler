#
# Project Euler Solution
# Problem ID: 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

def sum_multiples():
    multiples = [x for x in range(1000) if x % 3 == 0 or x % 5 == 0]
    return print(f'The sum of all multiples of 3 or 5 below 1000 is: {sum(multiples)}')

if __name__ == '__main__':
    sum_multiples()