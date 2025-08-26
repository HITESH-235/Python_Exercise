# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray. Return the sum of all subarray ranges of nums. A subarray is a contiguous non-empty sequence of elements within an array.
# LEETCODE link: https://leetcode.com/problems/sum-of-subarray-ranges/description/

def brute_force(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        largest = arr[i]
        smallest = arr[i]
        for j in range(i+1, n):
            largest = max(largest, arr[j])
            smallest = min(smallest, arr[j])
            total += largest-smallest
    return total
arr = [1,4,3,2]
print(brute_force(arr))


# Optimised version:

def PrevSmaller(arr):
    st = []
    res = []
    for i in range(len(arr)):
        while st and st[-1][0] >= arr[i]:
            st.pop()
        res.append(st[-1][1] if st else -1)
        st.append([arr[i],i])
    return res

def NextSmaller(arr):
    st = []
    res = [len(arr)]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while st and st[-1][0] > arr[i]: # not putting "=" in any one function avoids edge case mistake e.g. [1,1]
            st.pop()
        if st:
            res[i] = st[-1][1]
        st.append([arr[i],i])
    return res

def PrevGreater(arr):
    st = []
    res = []
    for i in range(len(arr)):
        while st and st[-1][0] <= arr[i]:
            st.pop()
        res.append(st[-1][1] if st else -1)
        st.append([arr[i],i])
    return res

def NextGreater(arr):
    st = []
    res = [len(arr)]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        while st and st[-1][0] < arr[i]: # not putting "=" in any one function avoids edge case mistake e.g. [1,1]
            st.pop()
        if st:
            res[i] = st[-1][1]
        st.append([arr[i],i])
    return res

def subarrayMin(arr):
    nse = NextSmaller(arr) # return list with indices of nearest smaller element
    pse = PrevSmaller(arr)
    total = 0
    mod = 10**9 + 7
    for i in range(len(arr)):
        left = i - pse[i]
        right = nse[i] - i # getting the range upto which arr[i] is minimum
        total += (right * left * arr[i])%mod
    return total%mod

def subarrayMax(arr):
    nge = NextGreater(arr) # return list with indices of nearest smaller element
    pge = PrevGreater(arr)
    total = 0
    mod = 10**9 + 7
    for i in range(len(arr)):
        left = i - pge[i]
        right = nge[i] - i # getting the range upto which arr[i] is minimum
        total += (right * left * arr[i])%mod
    return total%mod

def optimised(arr):
    mod = 10**9 + 7
    sum_Largest = subarrayMax(arr)
    sum_Smallest = subarrayMin(arr)
    return (sum_Largest - sum_Smallest)%mod

print(optimised(arr))