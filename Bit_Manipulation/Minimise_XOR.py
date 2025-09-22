# Minimise XOR: Given two positive integers num1 and num2, find the positive integer x such that: 
# x has the same number of set bits as num2, and, the value x XOR num1 is minimal. Return the integer x.
# LEETCODE link: https://leetcode.com/problems/minimize-xor/description/

def minimiseXOR(num1, num2):
    def countSetBits(num): # counts set bits so we can divide cases from values of c1, c2
        dup = num
        c = 0
        while dup != 0:
            dup &= dup-1
            c += 1
        return c
    c1 = countSetBits(num1)
    c2 = countSetBits(num2)

    if c1 == c2: return num1

    res = 0
    if c1 < c2: # cases where we have more 1s available in num2
        i = 0
        while c2 >0: 
            if num1 & (1<<i) != 0: # when ith bit is set, must add it to res
                res ^= (1<<i)
                c1 -= 1
                c2 -= 1
                i += 1
            else:
                if c2-c1 > 0: # settings bits in res even when num1 is unset (at i)
                    while c2-c1 > 0 and num1 & (1<<i) == 0: # doing it for rightmost unset bits
                        c2 -= 1
                        res += (1<<i)
                        i += 1
                else:
                    i += 1
    else:
        dup = num1 # cases where there are more set bits in num1 (hence not all can be reached)
        while c1-c2 > 0: # thus we toggle left most set bits from res
            dup &= (dup-1)
            c1 -= 1
        return dup # thus in this case result will be left most bits
    return res

def minimiseXOR_2(num1, num2):
    def countSetBits(num):
        dup = num
        c = 0
        while dup != 0:
            dup &= dup - 1
            c += 1
        return c
    c1 = countSetBits(num1)
    c2 = countSetBits(num2)
    if c1 == c2: return num1

    res = num1
    i = 0
    while c1 != c2:
        if c1 < c2 and (1<<i) & num1 == 0:
            res ^= 1<<i
            c1 += 1
        elif c1 > c2 and (1<<i) & num1 > 0:
            res ^= 1<<i
            c1 -= 1
        i += 1
    return res
        
# the difference in this process is that we already put res = num1, so res can have all set bits already from num1
# if num1 has less set bits (c1 < c2):
# then toggle all initial 0s in res (since res = num1 initially, we just need to toggle right 0s)

# if num1 has more set bits (c1 > c2):
# then toggle the extra 1s in res (extra 1s = c1-c2) from right side

print(minimiseXOR_2(79,74))
print(minimiseXOR_2(3,7))