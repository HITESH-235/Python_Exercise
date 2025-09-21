# POWER SET: print a list which is power set of given arr
# LEETCODE link: https://leetcode.com/problems/subsets/description/

def powerSet(nums): # TC:(2^N * N); SC:(N)
    n = len(nums)
    res = []

    for x in range(1 << n): # equiv to 2^n
        temp = []
        for i in range(n):
            if x & (1<<i) != 0: # checking if ith bit set or not
                temp.append(nums[i])
        res.append(temp)
        
    return res

print(powerSet([1,2,3]))

# from the numbers in range(0-->2^n), we only need those many digits as numbers in arr (here 3)
# 0 0 0 = no numbers from arr (empty list)
# 0 0 1 = {1}
# 0 1 0 = {2}
# 0 1 1 = {1,2}
# 1 0 0 = {3}
# 1 0 1 = {1,3}
# 1 1 0 = {2,3}
# 1 1 1 = {1,2,3}