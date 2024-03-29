"""
From : https://projecteuler.net/problem=2
Context : Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and
2, the first 10 terms will be:
                        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Goal : By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
even-valued terms.

Author : Alexandre Dorais
"""

# We notice : given the structure of the Fibonacci sequence, it starts with an odd and even number (1,2), and their sum
# gives an odd number. Then, an odd + an even gives another odd number. The following number is even since the previous
# two are odd. Finally, we once again get the sum of an odd and an even number, which gives us an odd number. Therefore,
# the structure of the sequence is given by the following pattern :
#                     odd, even, odd, odd, even, odd, odd, even, odd, odd, even, ...
# where every term a_(1+3n) at the position 1+3n (where a_0 = 1 and a_1 = 2, and starting with n=0) is an even number.

numbers = [1,2]
while numbers[-1] <= 4000000:
    L = len(numbers)
    numbers.append(numbers[L-1] + numbers[L-2])

even_numbers = [numbers[i] for i in range(len(numbers)) if i%3==1]
answer = sum(even_numbers)
print(answer)