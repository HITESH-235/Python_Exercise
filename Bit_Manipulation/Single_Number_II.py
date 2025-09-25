# SINGLE NUMBER-II
# In a given array, all numbers appears thrice, except for one, find that num

def singleNumberII_Hash(nums): #TC-N; SC-N
    map = {}
    for x in nums:
        map[x] = map.get(x,0) + 1
    for x,y in map.items():
        if y == 1:
            return x
# __________________________________________________________________________________________________________________________
def singleNumberII_BitIndex(nums): #TC-(32*N); SC-1
    n = len(nums)
    res = 0
    for bitIndex in range(0,32):
        count = 0
        for i in range(n):
            if nums[i] & (1<<bitIndex) != 0:
                count += 1
        if count % 3 == 1:
            res += 2**bitIndex
    return res
# __________________________________________________________________________________________________________________________
def singleNumberII_Sorting(nums): #TC-(NlogN) + (N/3); SC-1
    nums.sort()
    n = len(nums)
    i = 1
    while i<n:
        if nums[i] == nums[i-1]:
            i += 3
            continue
        else:
            return nums[i-1]
    return nums[-1]
# __________________________________________________________________________________________________________________________
def singleNumberII_BitManipulation(nums): #TC-N; SC-1 //Best solution
    ones = 0;
    twos = 0; 

    for num in nums:
        ones = (num ^ ones) & (~twos)
        twos = (num ^ twos) & (~ones)
    return ones

# __________________________________________________________________________________________________________________________
import random
from time import time
nums = list(range(1, 10**5 + 1)) + list(range(1, 10**5 + 1)) + list(range(1, 10**5 + 1)) + [10**5+2]
random.shuffle(nums)
start = time()
print(singleNumberII_Hash(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
start = time()
print(singleNumberII_BitIndex(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
start = time()
print(singleNumberII_Sorting(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
start = time()
print(singleNumberII_BitManipulation(nums), end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
# ______________________________________________________Procedure Explained:________________________________________________

# Bit Index method:  

# 1.suppose the unique number has a 0* at ith index in binary form
#   hence the total count of 1s going thru all nums will either be 0 or 3, 6, 9....
#   because even if one num has 1 at ith ind, then total 1s at ith will be 3

# 2.similarly suppose the unique num has a 1* at ith index in binary form
#   then the least count of 1s at ith will be atleast 1 or 4, 7, 10....
#   hence clearly this (count % 3) is(=) 1 if the unique num has 1 at ith index

# 3.hence if ith index(of uniq num) is 1--> count %3 is 1; or 0 if 0
#   but we need to check every index of binary forms of every num
#   hence one loop goes from 0-31, as normally integer have that many indexes at max only
#   and another nest loop for going through list to check the ith bitIndex of each num

# 4.inside this nest loop we will and count the 1s encountered through "check ith bit"
#   coming out of nest loop, if count is some multiple of 3 (or 0) then result has 0 at ith bitIndex
#   else it has 1 at ith bitIndex, return this result at end
# __________________________________________________________________________________________________________________________

# Sorting method:

# 1.sort the nums arr, so every triad of numbers are grouped except once
#   in simple case suppose the uniq num is somewhere b/w, e.g. [2,2,2,3,3,3,4,5,5,5]
#   we start looking from i=1 and each time we check if nums[i] == nums[i-1], with i+=3 steps

# 2.each step takes us to middle of each triad and hence 2=2, 3=3, and so on
#   at i=7, nums[i]=5; but nums[i-1]=4, hence we return nums[i-1], when they arent equal
#   but what about edge cases such as uniq num is at i=0, or at last?

# 3.if uniq is at i=0, then loop return it in first iteration only
#   and if it as last index, our loop fails to find nums[i] != nums[i-1]
#   in that case, after loop ends, return the last index of nums arr

# *TC: the time complexity here is NlogN + N/3 which is not greater than 32*N, as [log(b=2)(N=10^9) =~ 30] < 32
# __________________________________________________________________________________________________________________________

# Bit Manipulation method:

# 1.ones- mask to keep bits that have appeared one
#   twos- mask to keeps bits that have appeared twice

# 2.ones will be updated if the num is "not in twos"
#   twos will be updated if the num is "not in ones"
#   ones will have deletion if num appearing again with num already in ones
#   twos will have deletion if num appearing again with num already in twos

# 3.dont need threes as num is deleted from twos directly
#   finally ones store the num that appears once only
# __________________________________________________________________________________________________________________________