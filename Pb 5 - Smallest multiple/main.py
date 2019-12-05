"""
From : https://projecteuler.net/problem=5
Context : 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
Goal : What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers
from 1 to 20?

Author : Alexandre Dorais
"""


# As this problem is too easy, and doesn't even require a program, we will instead solve the general case, where we will
# be able to input a number (M), and the program will find the smallest number that is evenly divisible by all the
# numbers from 1 to M. We need to define a simple algorithm to do this.
# First : We will list all the prime numbers between 1 and M. This is referred to as list 1.
# Second : We will express each of the numbers from 1 to M with a list containing its prime factors.
# Third : For each of the prime numbers from list 1, we will look at all the lists generated in step 2, and find the
# maximum amount of occurrences of that prime number in a single number. For example, in our case from 1 to 20, we would
# look at the prime number 2, and notice that its maximum amount of occurrences in a single number is 4 times in the
# number 16.
# Fourth : We will calculate the answer as being the product of every prime number from 1 to M, raised to the power of
# the number of occurrences found in step 3.


def main():
    # Step 1
    M = int(input('We want the smallest number evenly divisible by every number between 1 and: '))
    prime_numbers = [2]
    prime_numbers = new_prime_numbers(3, M, prime_numbers)

    # Step 2
    prime_factorisation = [[1] for _ in range(M)]  # every number is divisible by 1
    for i in range(1, M + 1):
        flag = False
        quotient = i
        while not flag:
            for divisor in prime_numbers:
                if quotient % divisor == 0:
                    prime_factorisation[i - 1].append(divisor)
                    quotient = quotient / divisor
            if quotient == 1:
                flag = True  # we have found all the prime factors of the initial number

    # Step 3
    max_occurrences = [1 for _ in range(len(prime_numbers))]  # every prime factor is present at least one time
    for j in range(len(prime_numbers)):
        for i in range(1, M + 1):
            # count how many times prime_numbers(j) appears in prime factorisation of i
            occurrences = prime_factorisation[i - 1].count(prime_numbers[j])
            if occurrences > max_occurrences[j]:
                max_occurrences[j] = occurrences

    # Step 4
    answer = 1
    for j in range(len(prime_numbers)):
        answer = answer * prime_numbers[j]**max_occurrences[j]

    print(answer)


def new_prime_numbers(start, end, primes_list):
    for candidate in range(start, end+1):
        if all([(candidate % divisor != 0) for divisor in primes_list]):
            primes_list.append(candidate)
    return primes_list


main()
