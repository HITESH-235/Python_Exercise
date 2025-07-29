# You are given the root of a binary tree root. Invert the binary tree and return its root.
# LEETCODE link: https://leetcode.com/problems/invert-binary-tree/description/

def recursive_inversion(root):
    if not root:
        return
    else:
        left_node = root.left
        right_node = root.right
        root.right = left_node
        root.left = right_node
        recursive_inversion(left_node)
        recursive_inversion(right_node)


def dfs_inversion(root):
    if not root:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left # swapped
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def bfs_inversion(root):
    if not root:
        return
    queue = CustomQueue()
    queue.enqueue(root)
    while not queue.is_empty():
        node = queue.dequeue()
        node.left, node.right = node.right, node.left # swapped
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)


class TreeNode:
    def __init__(self, data):
        self.data = data            # data stored in the node
        self.left = None            # left child node
        self.right = None           # right child node
class BinarySearchTree:
    def __init__(self):
        self.root = None            # Root node of the binary search tree
    def insert_child(self,data):
        if not self.root:
            self.root = TreeNode(data)
            return
        current = self.root
        while current:
            if data < current.data:     # then add as left child node
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    return
            elif data > current.data:   # then add as right child node
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    return
            else: return
    def bfs(self):
        if not self.root:
            return None
        queue = CustomQueue()
        queue.enqueue(self.root)
        result = []

        while not queue.is_empty():
            temp = queue.dequeue()
            result.append(temp.data)
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)
        return result
class QueueNode:
    def __init__(self,data):
        self.data = data
        self.next = None 
class CustomQueue:
    def __init__(self):
        self.start = None
        self.end = None
    def enqueue(self,value):
        new_node = QueueNode(value)
        if self.is_empty():
            self.start = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = self.end.next
        return
    def dequeue(self):
        if self.is_empty():
            return None
        elif self.start == self.end:
            popped_node = self.start.data
            self.start = None
            self.end = None
            return popped_node
        else:
            popped_node = self.start.data
            self.start = self.start.next
            return popped_node
    def is_empty(self):
        return self.start is None
obj = BinarySearchTree()
obj.insert_child(10)
obj.insert_child(5)
obj.insert_child(3)
obj.insert_child(2)
obj.insert_child(4)
obj.insert_child(12)
obj.insert_child(9)
obj.insert_child(14)


print("Original Tree:", obj.bfs())

recursive_inversion(obj.root)
print("Inverted:", obj.bfs())

dfs_inversion(obj.root)
print("Inverted Again:", obj.bfs())

bfs_inversion(obj.root)
print("Inverted:", obj.bfs())