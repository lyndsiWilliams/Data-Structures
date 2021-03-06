from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
   - In an array/list, each element is independent and can be accessed using it's index.
     In a linked list, the element only has access to itself and the elements directly
     in front of and/or behind it, so methods needed to be created in order to mimic
     normal array/list methods.
"""


"""
# Array/List implementation
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # Return number of elements in the stack
        return self.size

    def push(self, value):
        # Add value to the top of the stack
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    def pop(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Remove element at the top of the stack
        # and assign it's value to popped variable
        popped = self.storage.pop()
        # Set size to storage list length
        self.size = len(self.storage)
        # Return popped value
        return popped
"""


# LinkedList implementation
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # Return number of elements in the stack
        return self.size

    def push(self, value):
        # Add value to the top of the stack
        self.storage.add_to_tail(value)
        # Add 1 to size value
        self.size += 1

    def pop(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Remove element's tail
        # and assign it's value to popped variable
        popped = self.storage.remove_tail()
        # Subtract 1 from size value
        self.size -= 1
        # Return popped value
        return popped
