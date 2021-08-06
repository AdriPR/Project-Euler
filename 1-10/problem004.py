#
# Project Euler Solution
# Problem ID: 4
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

# Finds the largest palindrome made from the product of two d-digit numbers
def largest_palindrome(d):
    res = 0

    for i in range(pow(10,d-1), pow(10, d)):
        for j in range(pow(10,d-1), pow(10, d)):
            n = i * j
            if str(n) == str(n)[::-1] and res < n:
                res = n

    return print(f'The largest palindrome made from the product of two {d}-digit numbers is: {res}')

if __name__ == '__main__':
    largest_palindrome(3)