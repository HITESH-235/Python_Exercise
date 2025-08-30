# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
# LEETCODE link: https://leetcode.com/problems/largest-rectangle-in-histogram/description/

def brute_force(heights):
    max_area = 0
    n = len(heights)
    for i in range(n):
        width = 1
        for j in range(i+1, n):
            if heights[j] >= heights[i]:
                width += 1
            else:
                break
        for j in range(i-1,-1,-1):
            if heights[j] >= heights[i]:
                width += 1
            else:
                break
        max_area = max(max_area, heights[i] * width)
    return max_area


def stack_implm(heights):
    st = []
    n = len(heights)
    max_area = 0
    for i in range(n):
        while st and st[-1][1] > heights[i]:
            element = st.pop()[1]
            nse = i
            pse = st[-1][0] if st else -1
            max_area = max(max_area, element*(nse-pse-1))
        st.append([i,heights[i]])
    while st:
        element = st.pop()[1]
        nse = n
        pse = st[-1][0] if st else -1
        max_area = max(max_area, element*(nse-pse-1))
    return max_area
heights = [2,1,5,6,2,3,7,8,3,2,4,4,21,3,3,35,4,5,2,23,23,4,23,43,5,54,4,5,75,3,63,6,3,33,46,45]

print(brute_force(heights))
print(stack_implm(heights))