# SINGLE NUMBER-III
# In a given array, all numbers appears twice, except for two numbers, return those numbers

def singleNumberIII_Hash(nums):
    res = []
    map = {}
    for x in nums:
        map[x] = map.get(x,0) + 1
    for x,y in map.items():
        if y == 1:
            res.append(x)
    return res[0],res[1]
# __________________________________________________________________________________________________________________________
def singleNumberIII_XOR(nums):
    XOR = 0
    for num in nums:
        XOR ^= num
    XOR = (XOR & (XOR-1)) ^ XOR 

    XOR_A = 0
    XOR_B = 0
    for num in nums:
        if (XOR & num) != 0:
            XOR_A ^= num
        else:
            XOR_B ^= num
    return XOR_A, XOR_B
# __________________________________________________________________________________________________________________________
from time import time
nums = list(range(1, 10**5 + 1)) + [10**5+2] + list(range(1, 10**5 + 1)) + [10**5+3]
start = time()
print(singleNumberIII_Hash(nums),end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
start = time()
print(singleNumberIII_XOR(nums),end=": ")
end = time()
print(f"{((end - start)*1000):.3f} milli-sec\n")
# ______________________________________________________Procedure Explained:________________________________________________
# Bit Manipulation method: Buckets:

# 1.Create a XOR for all elements of arr
#   finally we will have XOR of those two unique nums to be found
#   their XOR will have 1* wherever they are different
#   because we dont have to worry wherever they are same

# 2.Create a number with a set bit at index where XOR is set;
#   that can be done by using (x & (x-1)) which removes the rightmost set bit
#   and finally (x&(x-1))^x will create a number with only 1 bit set at that particular index where both nums differ

# 3.use this mask to find bucket of those numbers which are set at that index
#   and another bucket for numbers which are not set at that index
#   both buckets will have the two unique nums one each because that index had one num set and another unset

# 4.finally separate XOR of both buckets will lead both XORs to store the unique nums in different bucket
#   return those two XORs
# __________________________________________________________________________________________________________________________