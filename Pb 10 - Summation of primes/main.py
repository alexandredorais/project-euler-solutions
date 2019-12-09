"""
From : https://projecteuler.net/problem=8
Context : The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

                                    73167176531330624919225119674426574742355349194934
                                    96983520312774506326239578318016984801869478851843
                                    85861560789112949495459501737958331952853208805511
                                    12540698747158523863050715693290963295227443043557
                                    66896648950445244523161731856403098711121722383113
                                    62229893423380308135336276614282806444486645238749
                                    30358907296290491560440772390713810515859307960866
                                    70172427121883998797908792274921901699720888093776
                                    65727333001053367881220235421809751254540594752243
                                    52584907711670556013604839586446706324415722155397
                                    53697817977846174064955149290862569321978468622482
                                    83972241375657056057490261407972968652414535100474
                                    82166370484403199890008895243450658541227588666881
                                    16427171479924442928230863465674813919123162824586
                                    17866458359124566529476545682848912883142607690042
                                    24219022671055626321111109370544217506941658960408
                                    07198403850962455444362981230987879927244284909188
                                    84580156166097919133875499200524063689912560717606
                                    05886116467109405077541002256983155200055935729725
                                    71636269561882670428252483600823257530420752963450

Goal : Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of
this product?

Author : Alexandre Dorais
"""

# There isn't really much clever to do here, we will simply brute force the problem. One thing though, when looking for
# the largest product, instead of multiplying 13 digits every time, we will start off with the previous product, divide
# it by the number that will be discarded in the next product, and multiply that by the new digit. This will reduce the
# number of operations to solve the problem.

# Define the search grid (big number)
search_grid = ('73167176531330624919225119674426574742355349194934'
               '96983520312774506326239578318016984801869478851843'
               '85861560789112949495459501737958331952853208805511'
               '12540698747158523863050715693290963295227443043557'
               '66896648950445244523161731856403098711121722383113'
               '62229893423380308135336276614282806444486645238749'
               '30358907296290491560440772390713810515859307960866'
               '70172427121883998797908792274921901699720888093776'
               '65727333001053367881220235421809751254540594752243'
               '52584907711670556013604839586446706324415722155397'
               '53697817977846174064955149290862569321978468622482'
               '83972241375657056057490261407972968652414535100474'
               '82166370484403199890008895243450658541227588666881'
               '16427171479924442928230863465674813919123162824586'
               '17866458359124566529476545682848912883142607690042'
               '24219022671055626321111109370544217506941658960408'
               '07198403850962455444362981230987879927244284909188'
               '84580156166097919133875499200524063689912560717606'
               '05886116467109405077541002256983155200055935729725'
               '71636269561882670428252483600823257530420752963450')
search_grid = [int(search_grid[i]) for i in range(len(search_grid))]

# How many adjacent numbers do we want in the product
M = int(input('We are looking for the largest product of how many numbers: '))

# Define first product as previous_product and largest product yet as largest_product
previous_product = 1
for i in range(M):
    previous_product = previous_product * search_grid[i]
largest_product = previous_product  # this is not 0 for the given search grid
flag = False  # flag will be true if the previous product is 0

# Loop through the list to find the largest product
for i in range(1, len(search_grid) - M + 2):
    if all([search_grid[j] != 0 for j in range(i, i + M-1)]):  # make sure we don't multiply or divide by 0
        if not flag:
            previous_product = previous_product * search_grid[i + M - 1] // search_grid[i - 1]
            flag = False
        else:
            previous_product = 1
            for j in range(i, i + M):
                previous_product = previous_product * search_grid[j]
        if previous_product > largest_product:
            largest_product = previous_product
    else:
        flag = True  # the current product contains a 0

answer = largest_product
print(answer)