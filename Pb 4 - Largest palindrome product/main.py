"""
From : https://projecteuler.net/problem=4
Context : A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Goal : Find the largest palindrome made from the product of two 3-digit numbers.

Author : Alexandre Dorais
"""

# The following algorithm is actually to long, so we will not be using it. Instead, see algorithm at line 36.
# We will start with the number 999999 in descending order towards 11111, and we will identify any 6-digit or 5-digit
# palindromes we find and try to factor them into two 3-digit numbers. As soon as we are able to find one number which
# fit these requirements, it will be the largest by default.

"""
largest = 0
factor = 999
product = 999998

while largest == 0 and product >= 11111:
    possible = str(product)
    if possible[0] == possible[-1] and possible[1] == possible[-2] and possible[2] == possible[-3]:
        factor = 999
        while product % factor != 0 and factor >= 111:
            factor -= 1
        if factor * (product // factor) == product and 999 >= (product // factor) >= 111:
            largest = product
    else:
        product -= 1

if largest != 0:
    print(factor, " x ", (largest // factor), " = ", largest)
else:
    print('No palindrome number made from the product of two 3-digit numbers has been found.')
"""

# We will start with two numbers 999 and 999, multiply them, and check whether their product is a palindrome. If it is,
# we will remember it if it is the largest we have seen yet, and we'll also remember its factors.

palindrome = 0
factor1 = 0
factor2 = 0

for n1 in range(111,1000):
    for n2 in range(111,1000):
        possible = str(n1*n2)
        if possible[0] == possible[-1] and possible[1] == possible[-2] and possible[2] == possible[-3] and n1*n2 >= palindrome:
            palindrome = n1*n2; factor1 = n1; factor2 = n2

if palindrome != 0:
    print(factor1, " x ", factor2, " = ", palindrome)
else:
    print('No palindrome number made from the product of two 3-digit numbers has been found.')
