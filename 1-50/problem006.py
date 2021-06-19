#
# Project Euler Solution
# Problem ID: 6
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#

def sum_of_squares():
    x = 0
    y = 0
    for i in range(1,101):
        x = x + i
        y = y + pow(i, 2)
    return print(f'Solution: {pow(x,2) - y}')

if __name__ == '__main__':
    sum_of_squares()