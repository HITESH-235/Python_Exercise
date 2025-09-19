# Given an array of integers numbers that is sorted (increasing). Return the indices of two, [i, j], such that they i+j = t with i < j. exactly one valid solution.
# LEETCODE LINK: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def two_sum(lst,t):

    left = 0
    right = len(lst) - 1
    
    while left < right:
        x = lst[left]+lst[right]

        if x == t: return [left+1,right+1]
        elif x > t: right -= 1
        else: left += 1

    return "No Solution"

lst = [1,45,32,56,34,87,90,34,55,29,71,51,102,121,144]
print(two_sum(lst,145))

# ______________________________________________________Procedure Explained:______________________________________________________

# (keep in mind that given arr is sorted in ascending order)

# Two Pointer method:
# 1.initiate two pointers left and right with values 0 and n-1
#   run a while loop till left and right dont overlap
#   if nums[left] + nums[right] = t return left and right directly (since we have to return indices)

# 2.if not check if this expression is greater or smaller than target
#   if greater, we need to move to indexes with smaller numbers, hence decrease right
#   if smaller, we need to move to greater numbers, hence increase left (dont increase righ as we might skip )

# ________________________________________________________________________________________________________________________________