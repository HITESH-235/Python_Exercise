# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed. A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
# LEETCODE link: 

def brute_force(nums):
    nums = sorted(set(nums))
    max_count = 1
    count = 1
    if not nums:
        return 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count


def hashset(nums):
    items = set(nums)
    res = 0
    for num in items:
        if (num-1) not in items: # caught a starting of sequence
            count = 1
            while num+count in items:
                count += 1
            res = max(res, count)
    return res
nums = [1,3,4,6,24,5,7,8,8,9,0]


print(brute_force(nums))
print(hashset(nums))