# A queue has two main operations:
#
# Enqueue (Add): Adds an element to the end of the queue.
# Dequeue (Remove): Removes the element from the front of the queue.


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0


    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return 'queue is empty'


arr = []
obj = Queue()