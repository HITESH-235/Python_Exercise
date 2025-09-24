# Given an integer array nums, handle multiple queries of the following type: Calculate the sum of the elements of nums between indices left and right inclusive where left <= right. Implement the NumArray class:
# NumArray(nums) 
# sumRange(left, right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
# LEETCODE link: https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [0]

        for i in range(len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1]+nums[i])

    def sumRange(self, left, right):
        r = self.prefix_sum[right+1]
        l = self.prefix_sum[left]
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
        if i < left:
            left_sum += nums[i]
        if i == right:
            return right_sum - left_sum


import random
nums = [random.randint(-5, 20) for _ in range(20)]
print(nums)
right = 19
left = 0

print(sumRangeIntegrated(nums, left, right))
obj = NumArray(nums)
print(obj.sumRange(left, right))


# different way of asking the same question: A = [1,2,3,..], B=[[0,3],[1,2]....], res = [1+2+3+4, 2+3,...]
def sumRange_interviewbit(A,B):
    prefix_sum = [0]
    for i in range(len(A)):
        prefix_sum.append(prefix_sum[-1]+A[i])
    res = []
    for x,y in B:
        res.append(prefix_sum[y+1]-prefix_sum[x])
    return res

A = [1,2,3,4,5]
B = [[0,3], [1,2], [0,4]]
print(sumRange_interviewbit(A,B))