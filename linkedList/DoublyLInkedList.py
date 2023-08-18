class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            node.prev = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current

    def array_to_linkedList(self, arr):
        for i in arr:
            node = Node(i)
            if self.head is None:
                self.head = node
                node.prev = self.head
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
                node.prev = current

    def print_linkedList(self):
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next


obj = LinkedList()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
obj.array_to_linkedList(arr)
obj.print_linkedList()
