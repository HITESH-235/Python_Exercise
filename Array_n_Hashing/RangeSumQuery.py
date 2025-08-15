# Given an integer array nums, handle multiple queries of the following type: Calculate the sum of the elements of nums between indices left and right inclusive where left <= right. Implement the NumArray class:
# NumArray(nums) 
# sumRange(left, right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# LEETCODE link: https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray(object):
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = []
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            self.prefix_sum.append(temp)

    def sumRange(self, left, right):
        r = self.prefix_sum[right]
        l = self.prefix_sum[left] - self.nums[left]
        return r-l


def sumRangeIntegrated(nums, left, right):
    n = len(nums)
    if left < 0 or right < 0 or left > n or right > n or left > right:
        return False
    if left == right:
        return nums[left]

    left_sum = 0
    right_sum = 0

    for i in range(n):
        right_sum += nums[i]
        if i <= left:
            left_sum += nums[i]
        if i == right:
            return (right_sum - left_sum) + nums[left]


import random
nums = [random.randint(-5, 20) for _ in range(20)]
right = random.randint(5,19)
left = random.randint(0,right)

print(sumRangeIntegrated(nums, left, right))
obj = NumArray(nums)
print(obj.sumRange(left, right))