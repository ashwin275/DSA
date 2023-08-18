class Node:
    def __init__(self,value) :
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self) :
         self.head = None


    def add_node(self,value):
        node = Node(value)
        
        if self.head is None:
            self.head = node

        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node



    def add_node_begening(self,value,target):
        new_node = Node(value)

        if self.head.value == target:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head

            while current.next:
                if current.next.value == target:
                    new_node.next = current.next
                    current.next = new_node
                    current = current.next
                
                current = current.next
    def delete_node(self,value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next.value != value:
                current = current.next
            current.next = current.next.next

    def delete_before(self,value):
        if self.head.next.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next.next.value != value:
                current = current.next
            current.next = current.next.next

    def add_node_after(self,value,target):
        newnode = Node(value)
        if self.head.value == target:
            newnode.next = self.head.next
            self.head.next = newnode
        else:
            current = self.head
            while current.value != target:
                current = current.next
            newnode.next = current.next
            current.next = newnode






    def array_to_linkedlist(self,arr):
        for i in arr:
            node = Node(i)

            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next:
                    current = current.next

                current.next = node


    def print_node(self):
        current = self.head

        while current:
            print(current.value,end=' ')
            current = current.next
            


obj = LinkedList()
arr=[8,5,9,6,3,4,7]
obj.array_to_linkedlist(arr)
obj.add_node_after(89,6)
obj.print_node()
obj.add_node_begening(90,89)
print()
obj.print_node()
print()
obj.delete_node(90)
obj.print_node()
print()
obj.delete_before(7)
obj.print_node()