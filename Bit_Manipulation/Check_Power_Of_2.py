# Checking if no. is a power of 2 or not; return True or False
# Explained: such a number only has one 1s in it
# Hence if after remove the "last set bit" it becomes 0

def check_2Power(num):
    return num & num-1 == 0

print(check_2Power(1024))
print(check_2Power(1025))