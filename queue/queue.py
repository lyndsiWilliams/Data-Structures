from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


"""
# Array/List implementation
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        # Return number of elements in the queue
        return self.size

    # Adds an element to the back of the queue
    def enqueue(self, value):
        # Add value to the top of the queue
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    # Removes and returns the element at the front of the queue
    def dequeue(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Remove element at the top of the queue
        # and assign it's value to popped variable
        popped = self.storage.pop(0)
        # Set size to storage list length
        self.size = len(self.storage)
        # Return popped value
        return popped
"""


# LinkedList implementation
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # Return number of elements in the queue
        return self.size

    # Adds an element to the back of the queue
    def enqueue(self, value):
        # Add value to the top of the queue
        self.storage.append(value)
        # Set size to storage length
        self.size = len(self.storage)

    # Removes and returns the element at the front of the queue
    def dequeue(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Remove element at the top of the queue
        # and assign it's value to popped variable
        popped = self.storage.pop(0)
        # Set size to storage list length
        self.size = len(self.storage)
        # Return popped value
        return popped
