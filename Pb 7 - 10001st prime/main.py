"""
From : https://projecteuler.net/problem=7
Context : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
Goal : What is the 10 001st prime number?

Author : Alexandre Dorais
"""

# To solve this problem, we will simply use the same algorithm that we used for previous problems involving prime
# numbers. We will start off with a list containing the number 2 (the first prime number). Then, we will successively
# check every odd number that follows and verify whether it is cleanly divisible by any of the numbers in our list. If
# it isn't, then it is a prime, and we will add it to our list. We will go on until we have found the 10001st prime.

# input which prime number we want to know
n = int(input('We want the "n"th prime number: n = '))

prime_numbers = [2]
candidate = 3
while len(prime_numbers) < n:
    if any([(candidate % divisor == 0) for divisor in prime_numbers]):
        pass
    else:
        prime_numbers.append(candidate)
    candidate += 2

answer = prime_numbers[-1]
print(answer)


