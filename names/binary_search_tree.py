from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value against self
        if value == self.value:
            return True
        if value < self.value:
            # if empty
            if not self.left:
                # set left to node value
                self.left = BSTNode(value)
            else:
                # insert value to the left
                self.left.insert(value)
        else:
            # if empty
            if not self.right:
                # set right to node value
                self.right = BSTNode(value)
            else:
                # insert value to the right
                self.right.insert(value)

    def contains(self, target):
        # compared value against self
        if target == self.value:
            return True
        if target < self.value:
            # if left is empty
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            # if right is empty
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # values that are greater than are to the right
        # if empty
        if self.right is None:
            # return the value
            return self.value
        else:
            # return the max value
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the callback function fn on value
        fn(self.value)
        # if empty (note: test still pass without testing empty)
        if self.left is None and self.right is None:
            self.value
        # if left
        if self.left:
            self.left.for_each(fn)
        # if right
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if left (low)
        if node.left:
            self.left.in_order_print(node.left)
        print(node.value)
        # if right (high)
        if node.right:
            self.right.in_order_print(node.right)
        # print(f'value: {node.value}')

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = deque()
        # add the root node
        queue.append(self)
        # loop as long as the queue still has elements
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value) # or node.value

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []

        # add the root node
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            print(current.value) # or node.value

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
