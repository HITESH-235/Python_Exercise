# Nearest Smaller Element: Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than A[i]
# InterviewBit link : https://www.interviewbit.com/problems/nearest-smaller-element/
 
def brute_force(A):
    # stack = [-1]
    G = [-1]
    for i in range(1,len(A)):
        j = i-1
        # print(j,i)
        while j>=0 and A[j] >= A[i]:
            j -= 1
        G.append(A[j] if j>=0 else -1)
    return G


def stack_implm(A):
    stack = []
    G = []
    for i in range(len(A)):
        while stack and stack[-1] >= A[i]:
            stack.pop()
        G.append(stack[-1] if stack else -1)
        stack.append(A[i])
    return G


import random
from time import time
A = [random.randint(1,100) for _ in range(50)]

start = time()
print(brute_force(A))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(stack_implm(A))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")