from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
    # def __str__(self):
    #     return self.value

    # def __repr__(self):
    #     return self.value