# import sys
# sys.path.append('D:\\lambda\\PYTHON\\Data-Structures\\stack\\stack.py')
# from stack import Stack
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
    - The differences are almost the same as when one is implementing a Stack, except
    when removing and returning the element in the front. In a Stack, you've got to
    remove the tail; in a Queue, you've got to remove the head.
    - Stack must be add/removed from the SAME side, Queue must be add/removed from
    the OPPOSITE side.
   
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
        self.storage = LinkedList()

    def __len__(self):
        # Return number of elements in the queue
        return self.size

    # Adds an element to the back of the queue
    def enqueue(self, value):
        # Add value to the top of the queue
        self.storage.add_to_tail(value)
        # Add 1 to size value
        self.size += 1

    # Removes and returns the element at the front of the queue
    def dequeue(self):
        # Check if list is empty
        if self.size == 0:
            return None
        # Remove the element's head
        # and assign it's value to popped variable
        popped = self.storage.remove_head()
        # Subtract 1 from size value
        self.size -= 1
        # Return popped value
        return popped
