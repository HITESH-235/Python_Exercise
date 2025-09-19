# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1. Return the maximum area of water that can be trapped between the bars.
# LEETCODE link: https://leetcode.com/problems/trapping-rain-water/

# TC: O(3N); SC: O(N)
def trapping_water_Iterative(heights): # --> (int) as units of water trapped
    right_max = 0 # var to store max value from right
    suffix_max = [] # var to store right_max
    n = len(heights)

    for i in range(n-1, -1, -1):
        right_max = max(right_max, heights[i])
        suffix_max.append(right_max)

    suffix_max = suffix_max[::-1]

    left_max = 0
    total = 0

    for i in range(n):
        left_max = max(left_max, heights[i])
        total += min(left_max, suffix_max[i]) - heights[i]
    return total

# TC: O(N); SC: O(1)
def trapping_water_TwoPointer(heights):
    n = len(heights)
    left = 0
    right = n - 1
    left_max, right_max = 0, 0
    total = 0

    while left < right:
        left_max = max(left_max, heights[left])
        right_max = max(right_max, heights[right])

        if left_max < right_max:
            total += left_max - heights[left]
            left += 1
        else:
            total += right_max - heights[right]
            right -= 1
    return total


# Example Usage:
heights = []
import random
heights += [random.randint(0, 1000) for _ in range(500)]

from time import time
start = time()
print(trapping_water_Iterative(heights))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(trapping_water_TwoPointer(heights))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

# ______________________________________________________Procedure Explained:______________________________________________________

# Iterative method(takes extra space):
# 1.create a suffix max arr looping from reverse direction
#   dont forget to reverse the suffix max arr in python

# 2.run another loop for prefix max but we do not need to create another arr for that
#   just keep a track of max from left direction in loop
#   check which is smaller from current left max and right max
#   we call this curr max for now

# 3.we can store exactly that amount of water that is difference between curr height and curr max
#   this is because whichever from left max and right max is smaller decides the water we can keep
#   the greater of them simply doesnt affect the count

# 4.hence we can keep a total variable to count water units to be stored from each index(heights)
#   increase total with min(left_max, suffix_max[i]) - curr_height; (or heights[i])
#   return this total as answer
# ________________________________________________________________________________________________________________________________

# Two Pointer method:
# 1.create two vars named left max and right max to keep track of max's from both direction
#   in order to track from both direction we need two pointer approach

# 2.run a while loop till right pointer isnt equal or lesser than left pointer
#   similar to above method for checking if min of left max and right max
#   decrease curr height from the min found above
#   add this difference to total (answer), return total
# ________________________________________________________________________________________________________________________________