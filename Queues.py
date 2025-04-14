"""

THESE ARE THE KEY METHODS REQUIRED FOR A QUEUE:

enqueue(item) - Add an item to the end of the queue.
dequeue() - Remove and return the item from the front of the queue.
peek() - View the front item without removing it.
is_empty() - Check if the queue is empty.
is_full() (for limited queues ONLY) - Check if the queue has reached its maximum size.
size() - Return the number of items in the queue.


FIFO - First In First Out
e.g queueing in a shop
"""


class Queue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        """
        Here is a nice quick guide on what Map is:
        https://www.w3schools.com/python/ref_func_map.asp

        also a very good YT video on it and more:
        https://www.youtube.com/watch?v=hUes6y2b--0

        """
        if not self.is_empty():
            return "[FRONT] " + " <- ".join(map(str, self.queue)) + " [BACK]"
        else:
            return "Queue is empty"

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from empty queue")


# NOTE - Below is an example of a LIMITED Queue

class LimitedQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self, item):
        """Add an item to the end of the queue if there is space."""
        if self.size() < self.max_size:
            self.queue.append(item)
        else:
            raise OverflowError("Queue is full. Cannot add new item.")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def is_full(self):
        """Check if the queue is full."""
        return len(self.queue) == self.max_size

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from empty queue")







