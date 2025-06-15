# CONTAINS DUPLICATE: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# LEETCODE link: https://leetcode.com/problems/contains-duplicate/description/

#Method 1
def method1(lst):
    n = 0
    for x in lst:
        for y in lst:
            if (x==y):
                n += 1

    if n > len(lst):
        return True
    else:
        return False

# Method 2
def method2(lst):
    if (len(lst) != len(set(lst))):
        return True
    else:
        return False

#Method 3
def method3(lst):
    for x in lst:
        lst.remove(x)
        if x in lst:
            lst.append(x)
            return True
        lst.append(x)     #restoring list values (for later use correctly)
    return False

#Dictionary Method 4
def method4(lst):
    seen = {}   #empty dictionary
    for num in lst:
        if num in seen:
            return True
        seen[num] = True     #stores num-True pairs (as key-value)
    return False

lst = [1,2,2,3,4,5]
print(method1(lst))
print(method2(lst))
print(method3(lst))
print(method4(lst))
