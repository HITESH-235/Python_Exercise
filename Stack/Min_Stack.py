# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class:
# void push(int val) pushes the element val onto the stack. void pop() removes the element on the top of the stack. int peek() gets the top element of the stack. int getMin() retrieves the minimum element in the stack.
# LEETCODE link: https://leetcode.com/problems/min-stack/description/

class StackNode:
    def __init__(self, data, cur_min):
        self.data = data
        self.cur_min = cur_min
        self.next = None

class MinStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self,data):
        if self.is_empty():
            self.top = StackNode(data, data)
            return
        cur_min = self.top.cur_min
        cur_min = min(cur_min, data)
        new_node = StackNode(data, cur_min)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return
        self.top = self.top.next

    def getmin(self):
        return self.top.cur_min

    def peek(self):
        return self.top.data


obj = MinStack()
obj.push(10)
obj.push(2)
obj.push(-1)
obj.pop()
obj.push(3)
obj.push(6)
obj.push(-4)
obj.push(8)
obj.pop()
obj.push(5)
print(obj.getmin())
print(obj.peek())