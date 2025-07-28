# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false. Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.
# LEETCODE link: https://leetcode.com/problems/same-tree/description/

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

def isSameTree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data == t2.data:
        return isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)
    return False

tree_1 = BinarySearchTree()
tree_1.insert_child(10)
tree_1.insert_child(5)
tree_1.insert_child(3)
tree_1.insert_child(2)
tree_1.insert_child(4)
tree_1.insert_child(12)
tree_1.insert_child(9)
tree_1.insert_child(14)

tree_2 = BinarySearchTree()
tree_2.insert_child(10)
tree_2.insert_child(5)
tree_2.insert_child(3)
tree_2.insert_child(2)
tree_2.insert_child(4)
tree_2.insert_child(12)
tree_2.insert_child(9)
tree_2.insert_child(14)

tree_3 = BinarySearchTree()
tree_3.insert_child(10)
tree_3.insert_child(5)
tree_3.insert_child(3)
tree_3.insert_child(2)
tree_3.insert_child(4)
tree_3.insert_child(12)
tree_3.insert_child(9)
tree_3.insert_child(15)

print(isSameTree(tree_1.root, tree_2.root))
print(isSameTree(tree_2.root, tree_3.root))
    