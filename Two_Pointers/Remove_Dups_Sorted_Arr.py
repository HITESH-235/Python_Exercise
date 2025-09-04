# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
# LEETCODE link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# constraint - cant use extra space


def brute_force(nums):
    n = len(nums)
    i = 1
    while i<n:
        if nums[i] == nums[i-1]:
            nums.pop(i-1)
            n -= 1 # decreased size of array
        else:
            i += 1 # moves ahead only when different item encountered
    return n


def two_pointer(nums):
    n = len(nums)
    j = 0 # tracker for differennt items
    for i in range(1,n):
        if nums[i] != nums[j]: 
            j += 1 #moves ahead only when different item encountered
            nums[j] = nums[i] # puts different item in place of duplicate(first one)
    return j+1


nums = [1,1,2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,]
print(brute_force(nums))   
print(two_pointer(nums)) 