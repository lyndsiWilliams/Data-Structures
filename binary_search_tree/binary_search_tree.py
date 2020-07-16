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

# class BinarySearchTree:
#     def __init__(self, root=None):
#         self.root = root

# ^^^-- is the same as --vvv

# root = BSTNode(26) # Root is 26

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # We need to go left
            # if we see that there is no left child...
            if self.left is None:
                # wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise, there is a child
            else:
                # call the left child's `insert` method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see that there is no right child...
            if self.right is None:
                # wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise, there is a child
            else:
                # call the right child's `insert` method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if the target is equal to the current node's value
        if target == self.value:
            return True
        # Check if the left side exists and
        # if the target is less than the current node's value
        elif self.left and target < self.value:
            return self.left.contains(target)
        # Check if the right side exists and
        # if the target is greater than the current node's value
        elif self.right and target > self.value:
            return self.right.contains(target)
        # Otherwise, the target value doesn't exist in this tree
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Check if there's a right node
        if self.right:
            # Recursion to the right
            return self.right.get_max()
        # The value that comes out is the max
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # The recursive function:
        fn(self.value)

        # Check if there's a right node
        if self.right:
            # Recursion to the right
            self.right.for_each(fn)

        # Check if there's a left node
        if self.left:
            # Recursion to the left
            self.left.for_each(fn)



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
