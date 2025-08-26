# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# LEETCODE link: https://leetcode.com/problems/next-greater-element-i/description/


def brute_force(nums1,nums2):
    temp = {}
    n = len(nums2)
    for i in range(n):
        j = i+1
        temp[nums2[i]] = -1

        while j < n:
            if nums2[j] > nums2[i]:
                temp[nums2[i]] = nums2[j]
                break
            j+=1

    res = []
    for num in nums1:
        res.append(temp[num])
    return res


def stack_2(nums1, nums2):
    n2 = len(nums2)
    st = [nums2[-1]]
    temp = [-1 for _ in range(n2)]
    for i in range(n2-2,-1,-1):
        while st and nums2[i] >= st[-1]:
            st.pop()
        if st:
            temp[i] = st[-1]
        st.append(nums2[i])
    res = []
    for num in nums1:
        res.append(temp[nums2.index(num)])
    return res


def optimised(nums1, nums2):
    st = []
    map = {}
    for num in nums2:
        while st and st[-1] < num:
            smaller = st.pop()
            map[smaller] = num
        st.append(num)
    for num in st:
        map[num] = -1
    res = []
    for num in nums1:
        res.append(map[num])
    return res

nums1 = [2, 7, 13, 25, 30, 45, 60, 90, 120, 150]
nums2 = [2, 1, 7, 5, 13, 10, 25, 20, 30, 28, 45, 40, 60, 55, 90, 85, 120, 110, 150]
print("Brute force:",brute_force(nums1,nums2))
print("Stack:",stack_2(nums1,nums2))
print("Stack Optimised:",optimised(nums1, nums2))