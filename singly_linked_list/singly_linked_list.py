class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        # Returns current value of element
        return self.value

    def get_next(self):
        # Returns the value of the element after this element in the stack
        return self.next

    def set_next(self, new_next):
        # Sets the value of the next element to a usable variable
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        # Create a new Node from the value
        new_node = Node(value)
        # Check if the head and tail are empty
        # If both are empty, the whole stack is empty
        if self.head is None and self.tail is None:
            # Refer both head and tail to the single node
            self.head = new_node
            # Set the new node to be the tail
            self.tail = new_node
        else:
            # Set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # Reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # Check for empty linked list
        if self.head is None and self.tail is None:
            # If empty, go back on your merry way. Nothing to delete.
            return
        # If there's only one element in the linked list (no next element)
        # both head and tail are pointing at the same Node
        if not self.head.get_next():
            head = self.head
            # Delete the linked list's head reference
            self.head = None
            # Also delete the linked list's tail reference
            self.tail = None
            return head.get_value()
        # Assign current head's value to val variable
        val = self.head.get_value()
        # Set self.head to the Node after the current head
        self.head = self.head.get_next()
        # Return removed head value
        return val

    def remove_tail(self):
        # Check for empty linked list
        if self.head is None:
            # If empty, go back on your merry way. Nothing to delete.
            return
        # Assign current head to current variable
        current = self.head
        # Check if the list is only one element or None
        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()
        # Set current tail's value to value variable
        # So that the method returns the deleted value
        value = self.tail.get_value()
        # Set old self.head to be new self.tail
        self.tail = current
        # Set new tail's "next" to None, it's now last in line.
        self.tail.set_next(None)
        # Return deleted value
        return value

    def contains(self, value):
        # Make sure the head exists
        if not self.head:
            return False
        # Reference the node we're currently at
        current = self.head
        # Check if it's a valid node
        while current:
            # Return True if the current value matches the target value
            if current.get_value() == value:
                return True
            # Update the current node to it's next node
            current = current.get_next()
        # Return false if the target node isn't in the list
        return False

    def get_max(self):
        # Make sure the head exists
        if not self.head:
            return None
        # Reference to the current largest value
        max_value = self.head.get_value()
        # Reference to the current node
        current = self.head.get_next()
        # Check if it's a valid node
        while current:
            # Check if the current value is greater than the max_value
            if current.get_value() > max_value:
                # If so, update our max_value variable
                max_value = current.get_value()
            # Update the current node to the next node in the list
            current = current.get_next()
        # Return the max value
        return max_value
