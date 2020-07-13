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







# class Queue:
#     def __init__(self):
#         self.activeStack = Stack()
#         self.inactiveStack = Stack()
# ​
#     def __len__(self):
#         return len(self.activeStack)
# ​
#     # This method puts new items on the bottom of an empty stack
#     # and then flips the existing stack over on top of it.
#     # Older items end up in the middle, newer ones radiate outwards.
#     # For example, a 6-item stack would look like: (top) 5 3 1 4 2 6 (bottom)
#     def enqueue(self, value):
#         # Place on the bottom of an empty stack
#         self.inactiveStack.push(value)
#         # Flip the current stack over on top of new value
#         for _ in range(len(self.activeStack)):
#             self.inactiveStack.push(self.activeStack.pop())
#         # Reverse pointers to the two stacks
#         self.inactiveStack, self.activeStack = self.activeStack, self.inactiveStack
# ​
#     # The oldest item is always located in the top-middle of the stack
#     # It's the 3rd item in a stack of 5, 3rd in a stack of 6, 4th in a stack of 7
#     # This method flips the top of the stack onto a temporary stack,
#     # then extracts the middle value,
#     # then flips the temporary stack back on top of the main stack.
#     def dequeue(self):
#         length = len(self.activeStack)
#         if length is 0:
#             return None
#         # Flip over the (top half - 1) of the stack
#         for _ in range((length-1)//2):
#             self.inactiveStack.push(self.activeStack.pop())
#         # Extract the middle value (which is the oldest)
#         return_value = self.activeStack.pop()
#         # Flip the top of the stack back over
#         for _ in range(len(self.inactiveStack)):
#             self.activeStack.push(self.inactiveStack.pop())
#         return return_value