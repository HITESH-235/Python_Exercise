# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return (-1)
# LEETCODE link: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

def method2(nums):
    num = -1
    for x in nums:
        if (x > num) and (-x in nums):
            num = x
    return num
lst2 = [1,2,4,0,-2,4,8,8,2,4,3,2,3,2,5,5,-104,104,23,-234,234,-112,112]
# print(method2(lst2))
