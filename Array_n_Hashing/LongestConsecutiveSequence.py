# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed. A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements *do not* have to be *consecutive* in the original array.
# LEETCODE link: https://leetcode.com/problems/longest-consecutive-sequence/description/

def brute_force(nums):
    n = len(nums)
    max_count = 0
    # using 2 loops, one to iterate through elements, one to look for sequences with num as starter
    for i in range(n):
        count = 1
        num = nums[i]
        for _ in range(n): # loop for searching (num+1)s, looking for sequence starting from num
            if (num+1) in nums:
                count+= 1 # updating count in every sequence encountered
                num += 1
            else:
                break
        max_count = max(max_count, count)
    return max_count


def sorting_(nums): # simply sorting lets us do 1 loop
    # looking for (num+1)s, updating count with (+1) if found, (=1) otherwise
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
        if (num-1) not in items: # only checking for start of sequences, initialises count
            count = 1
            while (num + count) in items: # checks if next is present or not
                count += 1
            max_count = max(max_count, count) # updates max_count with curr count
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
    max_count = 0
    for num in nums:
        if map.get(num,0) == 0: # doing this so duplicates cannot be considered again
        # also we dont have to use defaultdict as we use get()
            left_end = map.get(num-1,0)
            right_begin = map.get(num+1,0)
            map[num] = left_end + right_begin + 1 # 1 is for curr's own count
            map[num - left_end] = map[num] # going to the beginning of sequence
            map[num + right_begin] = map[num] # going to the end of sequence
            max_count = max(max_count, map[num])
    return max_count


from time import time
import random
lst = list(range(0, 1000))
random.shuffle(lst)
start = time()
print(brute_force(lst), end=": Brute Force: ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(sorting_(lst), end=": Sorting: ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_set(lst), end=": Hash Set: ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_map(lst), end=": Hash Map: ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(hash_map_2(lst), end=": Hash Map-2: ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")



# “What if the array has duplicates and you need to count them?”
def longestseq_with_dups(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    map = {}
    count = 0
    for num in nums:
        if map.get(num,0) == 0:
            left_end = map.get(num-1,0)
            right_begin = map.get(num+1,0)
            map[num] = left_end + right_begin + freq[num]
            map[num - left_end] = map[num]
            map[num + right_begin] = map[num]
            count = max(count, map[num])
    return count


# ______________________________________________________Procedure Explained:______________________________________________________

# (Brute force, sorting, hash-map methods explained through comments)

# Hash Set:
# 1.Create a set* with all unique elements of nums, so that lookup at an index is of linear complexity
#   initiate max_count = 0, run a loop in nums
#   Search for num which is start of sequence, simply by condition (num-1) not in set

# 2.when num-1 is not found, initiate count = 1, and a while* loop
#   run the while loop till we can find (num+count) in set, increase count if so
#   check if this curr sequence count is greater than any sequence found earlier, through a var max_count (initially was 0)
#   return max_count
# ________________________________________________________________________________________________________________________________