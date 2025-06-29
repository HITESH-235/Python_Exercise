# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day. You may choose a single day to buy one stock and choose a different day in the future to sell it.Return the maximum profit you can achieve.
# Return 0 in case no profit can be made by selling
# LEETCODE link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

lst = [56, 34, 98, 2, 45, 78, 67, 23, 10, 100, 4, 80, 55, 54, 82, 51]

# def method_1(lst):
#     right = 0
#     arr = [0 for _ in range(len(lst))]

#     for x in range(len(lst),0,-1):

#         if lst[x-1] > right:
#             right = lst[x-1]
#         arr[x-1] = right

#     profit = 0
#     for x in range(len(lst)):

#         if profit < (arr[x] - lst[x]):
#             profit = (arr[x] - lst[x])

#     return profit
# print(method_1(lst))

def method_1(lst):
    max_right = 0
    profit = 0

    for x in range(len(lst)-1, -1, -1):

        if lst[x] > max_right:
            max_right = lst[x]

        profit = max(profit, max_right - lst[x])
    return profit
        
print(method_1(lst))
def method_2(lst):

    profit = 0
    for i in range(len(lst)):

        for j in range(i+1,len(lst)):

            if profit < lst[j]-lst[i]:
                profit = lst[j]-lst[i]

    return profit

print(method_2(lst))

def method_3(lst):
    left , right = 0 , 1

    profit = 0
    while len(lst) > right:

        if lst[left] < lst[right]:
            profit = max(profit,(lst[right]-lst[left]))
            
        else:
           left = right
        right += 1
    return profit

print(method_3(lst))

        
