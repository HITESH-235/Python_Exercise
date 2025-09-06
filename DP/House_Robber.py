# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# LEETCODE link: https://leetcode.com/problems/house-robber/description/

def rob(nums):
    T = [0,nums[0]] # initialising table with adding 0 then first item
    n = len(nums)
    for i in range(2,n+1): # following index according to table rather than nums
        rob1 = T[i-1] # skip the curr
        # when skipping the current item take the sum robbed till last house

        rob2 = T[i-2]+nums[i-1] # take the curr
        T.append(max(rob1,rob2))
    return T[-1]

import random
nums = [random.randint(0,100) for _ in range(1000)]
print(rob(nums))