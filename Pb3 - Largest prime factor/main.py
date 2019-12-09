"""
From : https://projecteuler.net/problem=3
Context : The prime factors of 13195 are 5, 7, 13 and 29.
Goal : What is the largest prime factor of the number 600851475143 ?

Author : Alexandre Dorais
"""

# The solution described in the following paragraph actually takes too long to solve. Therefore, we have come up with
# another quicker solution, which is described starting on line 42 of this file.
# To solve this problem, we will start off with the given number, and successively try to divide it by increasing
# divisors. Once a divisor divides the number without remainder, we will divide the number by this divisor to get a new
# quotient, and we know that that divisor will be a prime factor of the initial number (since the divisors are strictly
# increasing, our algorithm will find any prime factor before finding non-prime factors, because any non-prime factor
# is a multiplication of two or more prime factors, and therefore greater than these prime factors which the algorithm
# will find first. Since the algorithm divides the number by the divisor and continues its search on the quotient, it
# will be impossible for the algorithm to return non-prime divisors.)

"""
import numpy as np

number = 600851475143
quotient = number
prime_factors = []
i = 0

while i < quotient:
    i += 1
    if quotient % i == 0:
        prime_factors.append(i)
        quotient = quotient / i
        i = 0

if np.prod(prime_factors) == number:
    answer = max(prime_factors)
    print(answer)
else:
    print('Something\'s wrong...')
"""


# As that solution was taking too long to process, we have decided on another solution. We will first generate a list of
# the first n prime numbers, and we will look for divisors within that list, and if the algorithm is no longer able to
# find divisors in that list, we will continue to expand the list before continuing the search. This solution is much
# faster than the previous solution as it takes barely seconds to find the answer.

def main():
    number = 600851475143
    quotient = number
    prime_numbers = [2, 3, 5, 7, 11, 13]  # next prime number will be 17
    prime_factors = []

    flag = False
    while quotient != 1:
        if flag:
            # generate new prime numbers if the existing list does not provide any new divisors of our number
            prime_numbers = new_prime_numbers(prime_numbers[-1], prime_numbers[-1] + 10000, prime_numbers)
            flag = False

        while not flag:
            length_pf = len(prime_factors)
            for divisor in prime_numbers:
                if quotient % divisor == 0:
                    prime_factors.append(divisor)
                    quotient = quotient / divisor
            if len(prime_factors) == length_pf:
                flag = True  # a whole loop through our prime_numbers list did not give any new divisors

    # Check and print our answer
    if product(prime_factors) == number:
        answer = max(prime_factors)
        print(answer)
    else:
        print('Something\'s wrong...')


def new_prime_numbers(start, end, primes_list):
    for candidate in range(start, end, 2):  # candidates for new prime numbers are only the odd numbers starting with 17
        if all([True for divisor in primes_list if
                candidate % divisor != 0]):  # candidate is divisible by no prime factor
            primes_list.append(candidate)
    return primes_list


def product(a_list):
    result = 1
    for i in a_list:
        result = result * i
    return result


main()
