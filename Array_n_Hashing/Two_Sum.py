#TWO SUM:Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
#LEETCODE link: https://leetcode.com/problems/two-sum/description/

def method1(lst,t):
    ind = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if (i!=j) and (lst[i]+lst[j] == t):
                ind = [i,j]
                return ind
    return False

def method2(lst,t):
    seen = {}   #enumerate stores index-value as key-value pair in enumerate object
    for index,num in enumerate(lst): #can also type dict(enumerate(lst))
        num2 = t - num
        if num2 in seen:
            return seen[num2],index
        seen[num] = index #storing num-ind in seen as key-val
    return False

def method3(lst,t):
    seen = set()
    for num in lst:
        if (t - num) in seen:
            return lst.index(t-num),lst.index(num)
        seen.add(num)
    return False

lst = [5,28,-2,14,13]
t= 26
print(method1(lst,t)) #longer
print(method2(lst,t)) #shorter
print(method3(lst,t)) #does not work correct when both values are same
# e.g. if for t = 26, lst has 13 and 13 at diff indices
