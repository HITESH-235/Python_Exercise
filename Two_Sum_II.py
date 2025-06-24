# Given an array of integers numbers that is sorted (increasing). Return the indices of two, [i, j], such that they i+j = t with i < j. exactly one valid solution.
# LEETCODE LINK: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

def two_sum(lst,t):

    left = 0
    right = len(lst) - 1
    
    while left < right:
        x = lst[left]+lst[right]

        if x == t:
            return left+1,right+1
        
        elif x > t:
            r -= 1

        else:
            l += 1

    return "No Solution"

lst = [1,45,32,56,34,87,90,34,55,29,71,51,102,121,144]
print(two_sum(lst,145))
