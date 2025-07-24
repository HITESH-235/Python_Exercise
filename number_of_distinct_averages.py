# Return the number of distinct averages calculated using the above process. (with min and max items of the list)
# Note that when there is a tie for a minimum or maximum number, any can be removed.
# LEETCODE_link: https://leetcode.com/problems/number-of-distinct-averages/description/

def distinctAverages(nums):
    nums.sort()
    avg_set = set()
    left = 0
    right = len(nums)-1
    while left < right:
        avg_set.add(nums[left] + nums[right])
        left += 1
        right -= 1
    return len(avg_set)

lst = [9,5,7,8,7,9,8,2,0,7]
print(distinctAverages(lst))