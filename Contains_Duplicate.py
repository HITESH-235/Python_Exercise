#Contains Duplicate
#LEETCODE link: https://neetcode.io/problems/duplicate-integer?list=neetcode150

def fn(lst):
    dct = {}
    for x in lst:
        if x in dct:
            return x
        dct[x] = True
    return False
lst = [1,2,4,5,6,3]
print(fn(lst))
