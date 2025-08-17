# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed. A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# LEETCODE link: https://leetcode.com/problems/longest-consecutive-sequence/description/

def brute_force(nums):
    n = len(nums)
    max_count = 0
    for i in range(n):
        count = 1
        num = nums[i]
        for _ in range(n):
            if (num+1) in nums:
                count+= 1
                num += 1
        max_count = max(max_count, count)
    return max_count


def sorting_(nums):
    items = sorted(set(nums))
    count = 1
    max_count = 0
    for num in items:
        if (num+1) in nums:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count


def hash_set(nums):
    items = set(nums)
    max_count = 0
    for num in nums:
        if (num-1) not in items:
            count = 1
            while (num + count) in nums: # checks if next is present or not
                count += 1
            max_count = max(max_count, count) # updates max_count
    return max_count


from collections import defaultdict
def hash_map(nums): # updates the left and right of sequences and ignores middle items
    map = defaultdict(int)
    count = 0
    for num in nums:
        if not map[num]:
            map[num] = map[num-1] + map[num+1] + 1 # checks left and right count becoz middle wont matter
            map[num - map[num-1]] = map[num] # goes exactly to the beginning of sequence to increase its count
            map[num + map[num+1]] = map[num] # updates right boundary of sequence, if already seen
            count = max(count, map[num]) # the count of left and right of sequence gives correct answer
    return count


def hash_map_2(nums): # simpler
    map = dict()
    count = 0
    for num in nums:
        if map.get(num,0) == 0:
            left_end = map.get(num-1,0)
            right_begin = map.get(num+1,0)
            map[num] = left_end + right_begin + 1
            map[num - left_end] = map[num]
            map[num + right_begin] = map[num]
            count = max(count, map[num])
    return count


from time import time

lst = [2,20,4,10,3,4,5]
lst = [0,3,2,5,4,6,1,1]
start = time()
print(brute_force(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(sorting_(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_set(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_map(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_map_2(lst))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")