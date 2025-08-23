# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# LEETCODE link: https://leetcode.com/problems/next-greater-element-i/description/

def brute_force(nums):
    res = []
    n = len(nums)
    for i in range(n-1):
        j = i+1
        
        while j < n:
            if nums[j] > nums[i]:
                res.append(nums[j])
                j = n
            elif j == n-1:
                res.append(-1)
                j = n
            j+=1
    res.append(-1)
    return res


def stack_(nums):
    n = len(nums)
    st = [nums[-1]]
    res = [-1 for _ in range(n)]
    for i in range(n-2,-1,-1):
        while st and nums[i] >= st[-1]:
            st.pop()
        if st:
            res[i] = st[-1]
        st.append(nums[i])
    return res


nums = [6,10,8,3,4,5,5,2,6,2,84,74,2,6,7,9,10,56,3,4,6,7,8,4,5,6,3,6,4,5,456,6,3,6,4,334,6,7,433,6,3,6,34,34,34]
print(brute_force(nums))
print(stack_(nums))