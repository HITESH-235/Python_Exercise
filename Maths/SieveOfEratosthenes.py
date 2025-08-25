import math
def brute_force(num):
    res = []
    def prime(x):
        if x <= 1:
            return False
        if x % 2 == 0:
            return (x==2)
        for i in range(3, int(math.sqrt(x)+1),2):
            if x%i == 0:
                return False
        return True
    for i in range(2,num+1):
        if prime(i):
            res.append(i)
    return res

def optimised(num):
    map = {}
    for i in range(2,num+1):
        map[i] = 1

    for i in range(2,int(math.sqrt(num)+1)):
        if map[i] == 1:
            for j in range(i**2,num+1,i):
                map[j] = 0
    res = []
    for i,j in map.items():
        if j != 0:
            res.append(i)
    return res

num = 1000
# print(brute_force(31))
print(optimised(num))
print("Correct" if brute_force(num) == optimised(num) else "Wrong")
