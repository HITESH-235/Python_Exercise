# Given an integer N, find the XOR of all numbers from 1 to N

def XOROfRange_BF(n):
    XOR = 0
    for i in range(1,n+1):
        XOR ^= i
    return XOR

def XOROfRange_Optimised(n):
    XOR = 0
    if n%4 == 1: return 1
    elif n%4 == 2: return n+1
    elif n%4 == 3: return 0
    else: return n 

# e.g.
# 1.Initialization: n = 9, XOR = 0

# 2.Catching a pattern:
#   n = 1; XOR = 1
#   n = 2; XOR = 3
#   n = 3; XOR = 0
#   n = 4; XOR = 4

#   n = 5; XOR = 1
#   n = 6; XOR = 7
#   n = 7; XOR = 0
#   n = 8; XOR = 8

#   n = 9; XOR = 1

# 3.Clearly we can see that at (n%4 == 1-->2-->3-->0): ---> XOR is (1)*--> (n+1)*--> (0)*--> finally (n)*