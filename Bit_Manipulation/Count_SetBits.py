# Count the total set bits (1s) in num

def countSetBits_normal(num):
    count = 0
    while (num != 0):
        count += num & 1 # increase by 1 if 1 is rightmost
        num = num >> 1 # removing rightmost digit
    return count 

# another way to do is to remove rightmost set bit until num = 0
def countSetBits_Opt(num):
    count = 0
    while num != 0:
        num = num & (num-1)
        count += 1
    return count

from time import time
num = 4096**16-1
num = -53
start = time()
print(countSetBits_normal(num))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(countSetBits_Opt(num))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")