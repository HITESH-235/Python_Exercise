# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct. The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
# LEETCODE Link: https://leetcode.com/problems/3sum/description/

def brute_force(nums): # time complexity: n^3
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(n):
            if i != j:
                for k in range(n):
                    if i != k and j != k and nums[i]+nums[j]+nums[k] == 0:
                        if sorted([nums[i],nums[j],nums[k]]) not in res:
                            res.append(sorted(([nums[i],nums[j],nums[k]])))
    return res


def hash_map(nums): # time complexity: n^2
    n = len(nums)
    res_set = set()

    for i in range(n):
        seen = {}
        for j in range(n):
            if i == j:
                continue

            num_1 = nums[i]
            num_2 = nums[j]
            num_3 = -num_1 - num_2 # (x + y + z = 0) => (x = -y - z)

            if num_3 in seen:
                res_item = sorted([num_1, num_2, num_3])
                res_set.add(tuple(res_item))
            seen[num_2] = j
    result = []
    for item in res_set:
        result.append(list(item))
    return result


def sliding_window(nums): # time complexity: n^2
    nums.sort()
    result = []

    for index, current in enumerate(nums):
        if index > 0 and current == nums[index-1]: # shifts current to next
            continue

        left = index + 1 # avoid being same as current
        right = len(nums)-1

        while left < right:
            sum = current + nums[left] + nums[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([current, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right: # current already does work for same values
                    left += 1
    return result

lst = [2,6,23,5,-3,7,2,-8,4,8,0,0,0,-23] # [[6, 2, -8], [23, 0, -23], [8, 0, -8], [0, 0, 0]]

import time
print('\n')
start_time = time.time()
print("Brute Force:", brute_force(lst))
end_time = time.time()
print("1:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Using Hash Map:", hash_map(lst))
end_time = time.time()
print("2:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Using Sliding Window:", sliding_window(lst))
end_time = time.time()
print("3:", end_time - start_time, "seconds\n")