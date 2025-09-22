# Calculate the count of minimum bitflips need to be done to make num = target
# Explanation:
# XOR b/w num and target will create a binary num which has set bits only where num and target differ
# Hence just count the set bits in num ^ target 


def minBitFlips(num, target):
    temp = num ^ target
    count = 0
    while (temp != 0):
        temp = temp & (temp-1)
        count += 1
    return count


num1 = 0b1010101010110
num2 = 0b1100000110100
print(minBitFlips(num1, num2))