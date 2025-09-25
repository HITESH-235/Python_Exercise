# SINGLE NUMBER-I
# All numbers in an array appear twice except for one, return that num

def singleNumberI_Hash(nums): #TC-N; SC-N
    map = {};
    for x in nums:
        map[x] = map.get(x,0) + 1
    for x,y in map.items():
        if y == 1:
            return x

def singleNumberI_XOR(nums): #TC-N; SC-1
    XOR = 0
    for x in nums:
        XOR ^= x
    return XOR

import random
from time import time
nums = list(range(1, 10**5 + 1)) + [10**5+2] + list(range(1, 10**5 + 1))
random.shuffle(nums) # unique = 100002
start = time()
print(singleNumberI_Hash(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
start = time()
print(singleNumberI_XOR(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")