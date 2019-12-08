"""
From : https://projecteuler.net/problem=9
Context : A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
                                    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Goal : There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

Author : Alexandre Dorais
"""

# One interesting thing to note about Pythagorean triplets is that given a Pythagorean triplet (a,b,c) and any integer
# n, we also know that the triplet (na, nb, nc) is also a Pythagorean triplet. I strongly suspect the triplet we are
# looking for is constructed in this way, so we will first look for Pythagorean triplets where a and b are smaller than
# 50 and try to scale them up to find a sum of 1000, and if that doesn't work, we will keep exploring the higher
# Pythagorean triplets.
import numpy as np

target = 1000
triplets = []
i = 0
tolerance = 0.001

# Find small Pythagorean triplets
for a in range(1,50):
    for b in range(a, 50):
        if -tolerance < np.sqrt(a ** 2 + b ** 2) - round(np.sqrt(a ** 2 + b ** 2)) < tolerance:
            triplets.append([a, b, round(np.sqrt(a ** 2 + b ** 2))])
            i += 1

n = 0
raw_triplet = []

# Check if we can multiply a small Pythagorean triplet to get one that sums to 1000
for triplet in triplets:
    sum_of_triplet = int(sum(triplet))
    if target % sum_of_triplet == 0:
        n = target // sum_of_triplet
        raw_triplet = [int(j) for j in triplet]

final_triplet = [n * i for i in raw_triplet]
answer = np.prod(final_triplet)
print(n, ' x ', raw_triplet, ' = ', final_triplet)
print(answer)