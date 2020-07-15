"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Add 1 to length
        self.length += 1
        # Create a new ListNode from the value
        new_node = ListNode(value)
        # Check for empty list
        if self.head is None:
            # New node is the head of the list now
            self.head = new_node
            # Head and tail point to themselves since
            # this is the only item on the list now
            self.tail = self.head
        # List is not empty:
        else:
            # Set the new node's next to the old head (N)
            new_node.next = self.head
            # Set old head's prev to new node
            self.head.prev = new_node
            # Set old head to new node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Subtract 1 from length
        self.length -= 1
        # Assign current head's value to val variable
        val = self.head.value
        # Check if there's only one node
        if self.head is self.tail:
            # Delete both head and tail, since it's the only node
            self.head = None
            self.tail = None
            # Return deleted node
            return val
        else:
            # Set current node's head to the node after the current head
            self.head = self.head.next
            # Set current node's prev to None (disconnect from the list)
            self.head.prev = None
            # Return removed head value
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Add 1 to length
        self.length += 1
        # Create a new ListNode from the value
        new_node = ListNode(value)
        # Check for empty list
        if self.head is None and self.tail is None:
            # Head and tail both point to new node
            # Because there is now only one node in list
            self.head = new_node
            self.tail = new_node
        # List is not empty:
        else:
            # Set current node tail's next to the new node
            self.tail.next = new_node
            # Set new node's prev to current node's tail
            new_node.prev = self.tail
            # The new node is now the tail of the list
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Subtract 1 from length
        self.length -= 1
        # Get deleted tail's value for returning
        val = self.tail.value
        # Check for empty list
        if self.head is None and self.tail is None:
            # If empty, go back on your merry way. Nothing to delete.
            return None
        # Delete the current node
        self.tail = self.head = None
        # Return deleted value
        return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass