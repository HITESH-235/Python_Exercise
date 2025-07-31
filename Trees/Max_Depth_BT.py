# Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# LEETCODE link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/


def maxDepth_DfsRecursive(root):
    if not root:
        return 0
    return 1 + max(maxDepth_DfsRecursive(root.left), maxDepth_DfsRecursive(root.right))


def maxDepth_DfsIterative(root):
    if not root:
        return 0
    stack = [[root,1]]
    max_depth = 0
    while stack:
        cur_node, cur_depth = stack.pop()
        max_depth = max(max_depth, cur_depth)

        if cur_node.left:
            stack.append([cur_node.left, cur_depth+1])
        if cur_node.right:
            stack.append([cur_node.right, cur_depth+1])
    return max_depth


def maxDepth_Bfs(root):
    if not root:
        return 0
    queue = CustomQueue()
    queue.enqueue(root)
    depth = 0
    while queue.start:
        n = queue.cur_size
        for _ in range(n):
            cur_node = queue.dequeue()
            if cur_node.left:
                queue.enqueue(cur_node.left)
            if cur_node.right:
                queue.enqueue(cur_node.right)
        depth += 1
    return depth


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert_child(self,data):
        if not self.root:
            self.root = TreeNode(data)
            return
        current = self.root
        while current:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    return
            elif data > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    return
            else: return
class QueueNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class CustomQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.cur_size = 0
    def enqueue(self, data):
        self.cur_size += 1
        new_node = QueueNode(data)
        if not self.start:
            self.start = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = new_node
        return
    def dequeue(self):
        popped_node = self.start
        if not self.start:
            return
        elif self.start.data == self.end.data:
            self.cur_size = 0
            self.start, self.end = None, None
            return popped_node.data
        else:
            self.cur_size -= 1
            self.start = self.start.next
            return popped_node.data
        

# Example Usage:
tree = BinarySearchTree()
import random
for i in range(2000):
    x = random.randint(0, 1000)
    tree.insert_child(x)
from time import time
start = time()
print(maxDepth_DfsRecursive(tree.root))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(maxDepth_DfsIterative(tree.root)) # Best
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")

start = time()
print(maxDepth_Bfs(tree.root))
end = time()
print(f"{((end - start)*1000):.3f} milli-sec")