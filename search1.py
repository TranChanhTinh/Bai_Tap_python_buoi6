class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def search(self,target):
        current = self.head
        index=0
        while current:
            if current.value== target:
                return index
            current = current.next
            index +=1
        return -1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)

new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.search(20))