# Return the number of distinct averages calculated using the above process. (with min and max items of the list)
# Note that when there is a tie for a minimum or maximum number, any can be removed.
# LEETCODE_link: https://leetcode.com/problems/number-of-distinct-averages/description/

def method3(lst):
    lst.sort()
    avg_set = set()
    while len(lst)>0:
        num1 = lst.pop(0)
        num2 = lst.pop(len(lst)-1)
        # print("(",num1,",",num2,")")
        avg_set.add((num1+num2)/2)
    return len(avg_set)

lst3 = [1,2,5,3,2,2]
print(method3(lst3))
