# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day. The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day
# LEETCODE link: https://leetcode.com/problems/online-stock-span/description/


class BruteForce:

    def __init__(self):
        self.prices = []

    def next(self, price):
        self.prices.append(price)
        count = 0
        for i in range(len(self.prices)-1,-1,-1):
            if (self.prices[i] <= price):
                count += 1
            else:
                break
        return count

class StockSpanner: # otimised solution using stack

    def __init__(self):
        self.st = []
        self.ind = -1

    def next(self, price):
        self.ind += 1
        while self.st and self.st[-1][1] <= price: # remove until lesser or equal to get its index
            self.st.pop()
        ans = self.ind - (self.st[-1][0] if self.st else -1)
        self.st.append([self.ind, price])
        return ans

obj = BruteForce()
print(obj.next(7))
print(obj.next(1))
print(obj.next(2))
print(obj.next(9))
print(obj.next(3))
print(obj.next(4))
print(obj.next(8))
obj2 = StockSpanner()
print(obj2.next(7))
print(obj2.next(1))
print(obj2.next(2))
print(obj2.next(9))
print(obj2.next(3))
print(obj2.next(4))
print(obj2.next(8))
