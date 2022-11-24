import numpy as np
from tqdm import tqdm

pointers = {1: 1,
            4: 2,
            2: 1}  # (key: value) corresponds to (n: n/2 or 3*n+1 following Collatz rule)

lengths = {1: 0,
           4: 2,
           2: 1}  # (key: value) corresponds to (n: length of chain starting at n)

max_chain = 2
max_chain_int = 4
for i in tqdm(range(1, int(1e6))):
    len_path = 0
    new_num = i
    memory = []
    len_paths = []
    while new_num not in pointers.keys():
        memory.append(new_num)
        len_path += 1
        len_paths.append(len_path)
        pointers[new_num] = new_num//2 if new_num%2==0 else 3*new_num+1
        new_num = new_num//2 if new_num%2==0 else 3*new_num+1
    len_paths = [lp + lengths[new_num] for lp in len_paths]
    if len(len_paths) > 0 and len_paths[-1] > max_chain:
        max_chain = len_paths[-1]
        max_chain_int = i
    for num, lp in zip(memory[::-1], len_paths):
        lengths[num] = lp

    # if i not in pointers.keys():
    #     new_num = i/2 if i%2==0 else 3*i+1
    #     pointers[i] = new_num
    #     len_path += 1
    #     while new_num not in pointers.keys():
    #         pointers[new_num] = new_num/2 if new_num%2==0 else 3*new_num+1