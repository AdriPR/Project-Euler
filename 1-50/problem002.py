#
# Project Euler Solution
# Problem ID: 2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
#

def fibonacci():
    x = 0
    res = 0
    n = 1
    
    while n <= 4000000:
        if n % 2 == 0:
            res = res + n
        aux = x
        x = x + n 
        n = aux
        
    return print(f'The sum of even Fibonacci whose values do not exceed four million is: {res}')

if __name__ == '__main__':
    fibonacci()
