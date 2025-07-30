# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
# LEETCODE link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
def Counter(lst,t):
    lst.sort()
    left = 0
    right = len(lst)-1
    count = 0
    while left < right:
        if (lst[left]+lst[right])<t:
            count += right-left
            left += 1
        else:
            right -= 1
    return count

lst1 = [1,2,3,4,5,6,6,9,3,67,89,23,11,21,32,22,42,27,25]
t= 50
print(Counter(lst1,t))
