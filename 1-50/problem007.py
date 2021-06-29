#
# Project Euler Solution
# Problem ID: 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#

def is_prime(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def prime(pos):
    count = 0
    p = 2
    while count < pos:
        if is_prime(p):
            count = count + 1
        p = p + 1
    return print(f'Solution: {p-1}')

if __name__ == '__main__':
    prime(10001)