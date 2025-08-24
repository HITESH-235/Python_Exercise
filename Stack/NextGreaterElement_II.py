# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
# LEETCODE link: https://leetcode.com/problems/next-greater-element-ii/description/

def brute_force(nums):
    n = len(nums)
    res = [-1]*n
    for i in range(n):
        for j in range(i,2*n-1):
            j %= n
            if nums[j] > nums[i]:
                res[i] = nums[j]
                break
    return res


def stack_(nums):
    n = len(nums)
    st = []
    res = [-1]*n
    for i in range(2*n-1,-1,-1):
        while st and st[-1] <= nums[i%n]:
            st.pop()
        if i < n:
            if st:
                res[i] = st[-1]
        st.append(nums[i%n])
    return res


from time import time
import random
nums = [random.randint(1, 10**9) for _ in range(10**5)]

start = time()
x = brute_force(nums)
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
y = stack_(nums)
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")
if x == y:
    print("both are correct")