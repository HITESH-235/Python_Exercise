# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7
# LEETCODE link: https://leetcode.com/problems/sum-of-subarray-minimums/description/

def brute_force(arr):
    total = 0
    for i in range(len(arr)):
        least = arr[i]
        for j in range(i,len(arr)):
            least = min(least, arr[j])
            total += least
    return total


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

arr = [1,1]
def optimised(arr):
    nse = NextSmaller(arr) # return list with indices of nearest smaller element
    pse = PrevSmaller(arr)
    total = 0
    mod = 10**9 + 7
    for i in range(len(arr)):
        left = i - pse[i]
        right = nse[i] - i # getting the range upto which arr[i] is minimum
        total += (right * left * arr[i])/mod
    return total

arr = [1,1,1,2,3,4,4]
print(brute_force(arr))
print(optimised(arr))