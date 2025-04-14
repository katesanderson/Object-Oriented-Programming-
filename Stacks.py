"""

THESE ARE THE KEY METHODS REQUIRED FOR A QUEUE:

push(item): Add an item to the top of the stack.
pop(): Remove and return the item from the top of the stack.
peek(): View the top item without removing it.
is_empty(): Check if the stack is empty.
is_full() (for limited stacks ONLY) - Check if the stack has reached its maximum size.
size(): Get the current number of items in the stack.


LIFO - Last In First Out
e.g forwards or back only in a browser
ctrl z on a word document or redo/undo
"""


class Stack:
    def __init__(self):
        self.stack = []

    def __str__(self):
        """Return a string representation of the stack."""
        if self.is_empty():
            return "Stack is empty."
        else:
            return "[Bottom] " + " -> ".join(map(str, self.stack)) + " [TOP]"

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)


# NOTE - THIS IS AN EXAMPLE OF A LIMITED STACK

class LimitedStack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        """Add an item to the top of the stack if there is space."""
        if self.size() < self.max_size:
            self.stack.append(item)
        else:
            raise OverflowError("Stack is full. Cannot push new item.")

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        """Return the item at the top of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def is_full(self):
        """Check if the stack is full."""
        return len(self.stack) == self.max_size

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)
