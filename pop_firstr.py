def pop_first(self):
    if self.head is None:
        return None  # If the list is empty, there's nothing to pop

    popped_node = self.head
    self.head = self.head.next
    popped_node.next = None
    self.length -= 1  # Assuming `self.length` is the attribute representing the length of the list
    return popped_node
