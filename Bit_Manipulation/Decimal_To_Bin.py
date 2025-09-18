def cnvtToBin_BitMan(num,bits):
    if num < 0:
        num += (1<<bits)
    
    res = ""
    for i in range(bits-1,-1,-1):
        curr = (num>>i) & 1
        res += str(curr)
    return res

# ______________________________________________________Procedure Explained:________________________________________________

# 1.create a function which takes the number and number of bits as input, return binary in that many bit as a string
#   if the number is negative we can just add it to the largest number of its class, e.g. 2^8 = 256 for 8 bits,
#   then adding -5 to it makes (251) which is nothing but the same as -5 but in unsigned value
#   Hence the number is now the sum of its own value to 2^8 (or 1<<8)

# 2.Now we have to add trailing 0s or 1s to make the number 8 bits long
#   so we need to know the last index to store in res, which is nothing but (num >> i) where i ranges from bits-1 to 0
#   bits-1 because say we require the 1st index then we remove 7 bits from the num, where bits = 8
#   even if num doesnt have those many bits, then curr bit will automatically be 0 due to being & with 1
#   it is important to do (& 1) each time to not let any integer slip into res without conversion

# __________________________________________________________________________________________________________________________


# A beginner friendly way to convert minding signs as well
def convertToBin(num, bits):
    n = abs(num)
    def helper(n, bits, flag):
        res = ""
        if flag:
            while (n != 0):
                if n%2==1: res += "1"
                else: res += "0"
                n //= 2

            res += "0"
            trail = (bits-len(res))*"0"
        else:
            n -= 1
            while (n != 0):
                if n%2==1: res += "0"
                else: res += "1"
                n //= 2

            res += "1"
            trail = (bits - len(res))*"1" if (bits - len(res)) > 0 else None
        
        return trail+res[::-1] if trail else res[::-1]

    if num<0:
        return helper(n, bits, False)
    else:
        return helper(n,bits, True)


# example usage
print(cnvtToBin_BitMan(5,8) == convertToBin(5,8))
print(cnvtToBin_BitMan(-11,8) == convertToBin(-11,8))
print(cnvtToBin_BitMan(-100,32) == convertToBin(-100,32))
print(cnvtToBin_BitMan(10230,32) == convertToBin(10230,32))