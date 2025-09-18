# Set ith bit: return num; if already set; ignore: (OR)

def set_ith(num,i):
    mask = 1 << i
    return bin(num | mask)

print(set_ith(16,2)) # 16 = 10000, after setting 2nd: 10100