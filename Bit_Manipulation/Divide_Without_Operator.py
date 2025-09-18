# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Truncate the fractional part from the answer
# LEETCODE link: https://leetcode.com/problems/divide-two-integers/description/

def divideWithoutOperator_BF(dividend, divisor):
    temp = divisor
    count = 0
    while temp <= dividend:
        count += 1
        temp += divisor
    return count

print(divideWithoutOperator_BF(21,3))
# __________________________________________________________________________________________________________________________
def divideWithoutOperator_BitManipulation(dividend, divisor):
    # Handling edge cases:
    if dividend == 0: return 0
    elif dividend == divisor: return 1
    elif abs(dividend) < abs(divisor): return 0

    sign = (dividend > 0) == (divisor > 0) # true for + false for - sign

    n,d = abs(dividend), abs(divisor) # question is +num/+denom now
    def helper(n,d):
        if n<=d: return 1 if n==d else 0
        res = 0
        i = 0
        while d << (i+1) < n: i += 1

        n -= d << i     # d * 2**i
        res += 1 << i   # 2**i (adding quotient to res)

        if n >= d: # further division left if num is greater than denom
            res += helper(n, d)
        return res

    ans = helper(n,d)
    if sign: return ans if ans < 2**31 else 2**31-1
    else: return -ans if ans <= 2**31 else -2**31


print(divideWithoutOperator_BitManipulation(-5707680836,-69730))
print(divideWithoutOperator_BitManipulation(4,-4))

# ______________________________________________________Procedure Explained:________________________________________________

# Brute Force:
# 1.create a temp equal to divisor
#   increase temp (by divisor value) until it equals or exceed dividend's value
#   keep a count var to count each addition done, return count

# Bit Manipulation method:
# 1.handle edge cases such as when dividend is 0, or both are equal or dividend is smaller before main code
#   decide the sign to be given at end through storing true or false in a flag (sign)
#   create new vars to store +ve values of dividend and divisor

# 2.Run a while loop (iterative) till dividend is less than divisor, or try a helper function (recursion)
#   if loop, find largest power of two when multiplied with divisor, equal or smaller than dividend
#   do this using another loop, when found, decrease that (divisor*2**i) from dividend once out of loop
#   also, keep a res var which stores the quotients each time (2**i)

# 3.now check if dividend is greater-or-equal to divisor or not, return if not
#   if it is greater, the outer loop will run again till dividend is smaller than divisor

# * we can do this through recursion* by calling function again if dividend is still greater or equal
#   the helper function should return res as when they are called, res will be updated by what they(inner func) return
#   eventually, dividend becomes smaller than divisor, and recursion stops
#   all function will start return into parent (outermost) function

# 4.at the end, call the helper function, or use res (in iterative) directly
#   put the sign, do any necessary modulars required (here domain was -2**31 to 2**31-1)
# __________________________________________________________________________________________________________________________