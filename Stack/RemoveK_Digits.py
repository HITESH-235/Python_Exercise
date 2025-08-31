# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.
# LEETCODE link: https://leetcode.com/problems/remove-k-digits/description/

def brute_force(num,k):
    if k == 0:
        return num.lstrip("0") if int(num) != 0 else "0"
    if len(num) <= k:
        return "0"
    
    least = None
    for i in range(len(num)):
        curr = brute_force((num[:i]+num[i+1:]),k-1)
        if least is None or int(least) > int(curr):
            least = curr
    return least


def stack_(num, k):
    n = len(num)
    if n <= k:
        return "0"

    st = []
    for i in range(n):
        while st and k>0 and ord(st[-1])>ord(num[i]):
            st.pop()
            k -= 1
        st.append(num[i])

    while k > 0:
        st.pop()
        k -= 1
    if not st:
        return "0"

    res = ""
    flag = 0
    for item in st:
        if flag == 0 and item == "0":
            continue
        else:
            flag = 1
            res += item

    return res if res else "0"


num = "9876543210" * 10000 + "000000" + "1234567890" * 10000
k = 179880
print(stack_(num,k))

num = "1000123"
k = 4
print(brute_force(num,k)) # wont work for very large test cases