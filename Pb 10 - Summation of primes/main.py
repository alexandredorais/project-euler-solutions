"""
From : https://projecteuler.net/problem=10
Context : The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Goal : Find the sum of all the primes below two million.

Author : Alexandre Dorais
"""

# We will brute force this problem. We will simply find all the primes below 2 million and add them all up.

"""
prime_numbers = [2]
sum_of_primes = 2
candidates = [i for i in range(3,2000000,2)]
candidate = candidates[0]

while candidate < 5000:
    if any([candidate % prime == 0 for prime in prime_numbers]):  # if candidate is not prime
        candidates = candidates[1:]  # remove checked candidate from list
    else:  # if it is prime
        prime_numbers.append(candidate)
        sum_of_primes += candidate
        # remove all elements divisible by the new prime from candidates
        candidates = [i for i in candidates if i % candidate != 0]
        print(candidate)
        print('length ', len(candidates))

    candidate = candidates[0]

for candidate in range(5001, 2000000, 2):
    if any([candidate % prime == 0 for prime in prime_numbers]):  # if candidate is not prime
        pass
    else:
        prime_numbers.append(candidate)
        sum_of_primes += candidate
        print(candidate)

answer = sum_of_primes
print(answer)
"""

# Brute force takes too long, let's try a prime sieve algorithm. This next algorithm takes about 2 seconds in comparison
# to the multiple hours of the previous algorithm. It was all about the way we represented our data. This new way means
# we don't have to perform a million checks to verify if a new number is prime or not. Starting with a list with every
# number from 0 to 2000000, every time we encounter a non-zero element, it must be prime, because each time we find a
# prime, we remove from the list every multiple of it below 2000000 (by equating them to 0). This is the key that speeds
# up the algorithm : instead of removing the elements from the list, you equate them to 0. This makes it easier to keep
# track of primes and non-primes without having to check if a new number is divisible by all the previous ones.

max_number = 2000000
prime_numbers = list(range(max_number+1))
prime_numbers[1] = 0  # 1 is not prime

for prime in prime_numbers:
    if prime:
        for multiplier in range(prime, max_number // prime + 1):
            prime_numbers[prime * multiplier] = 0

answer = sum(prime_numbers)
print(answer)
