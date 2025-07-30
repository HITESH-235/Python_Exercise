# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.
# LEETCODE link: https://leetcode.com/problems/reverse-linked-list/description/


def reverse_iterative(linked_lst):
    temp = linked_lst.head
    prev = None
    while temp:
        front = temp.next
        temp.next = prev # links current head to none in first loop
        prev = temp
        temp = front
    linked_lst.head = prev


def reverse_recursive(linked_lst):
    def helper(node):
        if not node or not node.next:
            linked_lst.head = node
            return node

        new_head = helper(node.next)        # goes till leaf
        front = node.next                   # front and new_head represent same in deepest recursion, while head is just before it
        front.next = node                   # now the leaf's next is current node itself (reversed)
        node.next = None
        return
    helper(linked_lst.head)


def reverse_from_node(linked_lst, data):
    def helper(node):
        if not node or not node.next:
            return node
        new_head = helper(node.next)
        front = node.next
        front.next = node
        node.next = None
        return new_head

    if linked_lst.head.data != data:
        temp = linked_lst.head
        while temp.next.data != data:
            temp = temp.next
        temp.next = helper(temp.next)
    else:
        linked_lst.head = helper(linked_lst.head)
    return


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def return_lst(self):
        if self.head is None:
            print("Linked List Empty!")
            return
        itr = self.head
        ll_str = ""
        while itr is not None:
            ll_str += str(itr.data) + "-->"
            itr = itr.next
        return ll_str
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data)
        return
obj = LinkedList()
obj.insert_at_end(1)
obj.insert_at_end(3)
obj.insert_at_end(5)
obj.insert_at_end(7)
obj.insert_at_end(9)
obj.insert_at_end(10)
obj.insert_at_end(11)
obj.insert_at_end(13)


# Example Usage:
print("Original List:", obj.return_lst())
reverse_recursive(obj)
print("\nCompletely Reversed (Recursive):", obj.return_lst())
reverse_iterative(obj)
print("\nCompletely Reversed (Iterative):", obj.return_lst())
reverse_from_node(obj, 9)
print("\nReversed from (9):", obj.return_lst())