# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# LEETCODE link: https://leetcode.com/problems/binary-search/description/


def recursive_search(nums, target):
    def helper(left, right):
        if left > right: # for not in list
            return -1
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            return helper(left, mid-1)
        else:
            return helper(mid+1, right)

    left = 0
    right = len(nums)-1
    return helper(left, right)


def iterative_search(nums, target): # simpler to understand
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid-1
        else:
            left = mid+1
    return -1


lst = [-1,0,2,4,6,8]
print(recursive_search(lst, 10))
print(iterative_search(lst, 10))