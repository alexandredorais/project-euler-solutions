"""
From : https://projecteuler.net/problem=6
Context : The sum of the squares of the first ten natural numbers is,
                12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
                (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
                3025 − 385 = 2640.
Goal : Find the difference between the sum of the squares of the first one hundred natural numbers and the square of
the sum.

Author : Alexandre Dorais
"""

# This problem could seem complicated at first glance, especially if we replace the first hundred natural numbers by the
# first thousand, or the first million natural numbers. Then, it would seem like we would have to calculate the two
# gigantic sums and then find their difference. However, there actually exists a closed-form expression to calculate the
# sum of the first n natural numbers. We have that sum(1,2,3,...,n) = n*(n+1)/2. For example, sum(1) = 1*2/2 = 1;
# sum(1,2) = 2*3/2=3; sum(1,2,3) = 3*4/2 = 6, etc. In the same way, there also exists a simple expression to calculate
# the sum of the first n square numbers. We have that sum(1^2,2^2,3^2,...,n^2) = n*(n+1)*(2n+1)/6. For example
# sum(1^2) = 1*2*3/6 = 1; sum(1^2,2^2) = 2*3*5/6 = 5; sum(1^2,2^2,3^2) = 3*4*7/6 = 14, etc. This problem has thus become
# ridiculously easy with this simple trick.

# Input the upper number (100 in our case)
M = int(input('We want the difference between the sum of the squares and the square of the sum of the numbers from 1 to : '))

# Calculate sum of squares
sum_squares = M*(M+1)*(2*M+1)/6

# Calculate square of the sum
square_of_sum = (M*(M+1)/2)**2

# Calculate the difference between the two
answer = int(square_of_sum - sum_squares)
print(answer)


