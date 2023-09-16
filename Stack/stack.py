# A stack is a data structure that follows the Last-In-First-Out (LIFO) principle.
# This means that the last item added to the stack is the first one to be removed.
# Think of a stack of books, where you can only remove the topmost book

# --------Operations on a Stack-------:
# Push: Adds an item to the top of the stack.
# Pop: Removes the top item from the stack.
# Peek (or Top): Returns the top item from the stack without removing it.
# isEmpty: Checks if the stack is empty.
# Size: Returns the number of elements in the stack.


class stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            return  IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return  self.stack[-1]
        else:
            return  IndexError("stack is empty")


arr = [10,20,30,40,50]
obj = stack()
for i in arr:
    obj.push(i)

print(obj.stack)