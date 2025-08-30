# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
# LEETCODE link: https://leetcode.com/problems/maximal-rectangle/description/

def brute_force(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_area = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                min_width = float('inf')
                for k in range(i, n):
                    if matrix[k][j] == 0:
                        break
                    width = 0
                    for l in range(j, m):
                        if matrix[k][l] == 1:
                            width += 1
                        else:
                            break
                    min_width = min(min_width, width) # keep the smallest width so far(rows)
                    height = k-i+1 # current columns involved in width
                    max_area = max(max_area, height*min_width)
    return max_area


def stack_histogram(matrix):
    n = len(matrix) # rowa
    m = len(matrix[0]) # columns
    prefix_sum = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        sum = 0
        for j in range(n):
            if matrix[j][i] == 1:
                sum += 1
            else:
                sum = 0
            prefix_sum[j][i] = sum

    def helper(heights):
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
    
    maximal = 0
    for i in range(len(prefix_sum)):
        maximal = max(maximal,helper(prefix_sum[i]))
    return maximal


matrix = [[0, 1, 1], 
          [1, 1, 1], 
          [1, 1, 1], 
          [0, 0, 1]]
import time
import random
n, m = 10000, 10000
matrix = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

start = time.time()
# print(brute_force(matrix))
end = time.time()
print(f"{((end- start)*1000):.3f} milli-sec\n")

start = time.time()
print(stack_histogram(matrix))
end = time.time()
print(f"{((end- start)*1000):.3f} milli-sec\n")