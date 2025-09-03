# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# LEETCODE link: https://leetcode.com/problems/remove-k-digits/description/

def brute_force(num,k):
    if k == 0:
        return num.lstrip("0") if int(num) != 0 else "0" # trims of left 0s every time called
    if len(num) <= k: # for cases like this every digit is lost
        return "0"
    
    least = None
    for i in range(len(num)):
        curr = brute_force((num[:i]+num[i+1:]),k-1) # checks and remove every index till num is None
        if least is None or int(least) > int(curr): # updates least with min value of current num
            least = curr
    return least


def stack_(num, k):
    n = len(num)
    if n <= k:
        return "0"

    st = [] # will contain every digit except the smaller digits that come
    for i in range(n):
        while st and k>0 and ord(st[-1])>ord(num[i]):
            st.pop()
            k -= 1
        st.append(num[i]) # only digits greater than st[-1] gets appended

    while k > 0: # hence if we remove the last digits in st we are removing the greatest digits currently in st
        st.pop()
        k -= 1
    if not st: # we might* remove every element
        return "0"

    res = ""
    flag = 0 # using flag to ignore left 0s
    for item in st:
        if flag == 0 and item == "0": # if flag still not flipped and item 0 then it is a left 0 
            continue
        else:
            flag = 1 # if flag flipped then some other number came and now left 0s are finished
            res += item

    return res if res else "0"


num = "9876543210" * 10000 + "000000" + "1234567890" * 10000
k = 179880
print(stack_(num,k))

num = "1000123"
k = 4
print(brute_force(num,k)) # wont work for very large test cases