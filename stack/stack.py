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
   - In an array, each element is independent and can be accessed using it's index.
     In a linked list, the element only has access to itself and the elements directly
     in front of and/or behind it.
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # Return current size
        return self.size

    def push(self, value):
        # Add value to the end of storage list
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    def pop(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Assign popped value to popped variable
        popped = self.storage.pop()
        # Set size to storage list length
        self.size = len(self.storage)
        # Return popped value
        return popped
