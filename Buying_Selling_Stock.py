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


def max_profit_brute_force(prices):
    # Time: O(n^2), Space: O(1)
    max_profit = 0

    for buy_day in range(len(prices)):
        for sell_day in range(buy_day+1, len(prices)):
            current_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, current_profit)

    return max_profit


def max_profit_sliding_window(prices):
    # Time: O(n), Space: O(1)
    buy_day = 0
    sell_day = 1
    max_profit = 0

    while sell_day < len(prices):
        if prices[sell_day] > prices[buy_day]:
            current_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(max_profit, current_profit)
        else: 
            buy_day = sell_day # cases where buy_price > sell_price, updated buy_day
        sell_day += 1

    return max_profit


def max_profit_min_price(prices):
    # Time: O(n), Space: O(1)
    min_price = float('inf') #infinity representation
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit


def max_profit_right_max_array(prices):
    # Time: O(n), Space: O(n)
    n = len(prices)
    max_future_price = 0
    max_future_price_from_right = [0 for _ in range(n)]

    for i in range(n-1,-1,-1):
        max_future_price = max(max_future_price, prices[i])
        max_future_price_from_right[i] = max_future_price

    max_profit = 0
    for i in range(n):
        current_profit = max_future_price_from_right[i] - prices[i]
        max_profit = max(max_profit, current_profit)

    return max_profit


def max_profit_reverse_traversal(prices):
    # Time: O(n), Space: O(1)
    max_future_price = 0
    max_profit = 0

    for i in range(len(prices) - 1, -1, -1):
        max_future_price = max(max_future_price, prices[i])
        profit = max_future_price - prices[i]
        max_profit = max(max_profit, profit)

    return max_profit


prices = [56, 34, 98, 2, 45, 78, 67, 23, 10, 100, 4, 80, 55, 54, 82, 51]
import time
start_time = time.time()
print("Brute Force:", max_profit_brute_force(prices))
end_time = time.time()
print("1:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Sliding Window:", max_profit_sliding_window(prices))
end_time = time.time()
print("2:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Min Price Tracking:", max_profit_min_price(prices))
end_time = time.time()
print("3:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Right Max Array:", max_profit_right_max_array(prices))
end_time = time.time()
print("4:", end_time - start_time, "seconds\n")

start_time = time.time()
print("Reverse Traversal:", max_profit_reverse_traversal(prices))
end_time = time.time()
print("5:", end_time - start_time, "seconds\n")