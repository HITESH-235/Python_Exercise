# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i]. Each product is guaranteed to fit in a 32-bit integer.
# LEETCODE link: https://leetcode.com/problems/product-of-array-except-self/description/
# Constraint: Can't use division


def brute_force(nums): # O(n^2) complexity
    n = len(nums)
    res = []

    for i in range(n):
        product = 1
        for j in range(n):
            if j == i:
                continue
            product *= nums[j]
        res.append(product)
    return res


def prefix_suffix(nums): # O(n) complexity
    n = len(nums)
    if n == 1 or n == 0 or n == 2:
        return nums[::-1]
    # suffix pass
    suffix_arr = [1] * n
    suffix_arr[-1] = nums[-1]
    for i in range(n-2, -1, -1):
        suffix_arr[i] = suffix_arr[i+1] * nums[i]
    # prefix pass
    prefix_prod = nums[0]
    res = [suffix_arr[1]]
    for i in range(1, n-1):
        suffix_prod = suffix_arr[i+1]
        res.append(prefix_prod * suffix_prod)
        prefix_prod *= nums[i]

    res.append(prefix_prod)
    return res


def prefix_suffix_2(nums): # simpler to understand
    n = len(nums)
    res = [1] * n

    prefix_prod = 1
    for i in range(n):
        res[i] = prefix_prod
        prefix_prod *= nums[i]

    suffix_prod = 1
    for i in range(n-1, -1, -1):
        res[i] *= suffix_prod
        suffix_prod *= nums[i]
    return res


# Example Usage:
import random
import time
nums = []
for i in range(1000):
    nums.append(random.randint(1,9))

start = time.time()
print("Brute Force:", brute_force(nums), end=": ")
end = time.time()
print(f"{((end - start)*1000):.3f} milli-sec\n")

start = time.time()
print("Prefix-Suffix:", prefix_suffix(nums), end=": ")
end = time.time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time.time()
print("Prefix-Suffix-2:", prefix_suffix_2(nums), end=": ")
end = time.time()
print(f"{((end - start)*1000):.3f} milli-sec")