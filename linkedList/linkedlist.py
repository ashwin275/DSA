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
obj.add_node_begening(896,4)
obj.print_node()