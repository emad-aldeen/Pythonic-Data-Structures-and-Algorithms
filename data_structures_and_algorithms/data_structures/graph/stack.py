from data_structures_and_algorithms.data_structures.graph.queue import Node

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top == None:
            return True
        return False

    def push(self, value):
        new_node = Node(value)
        new_node.next, self.top = self.top, new_node

    def pop(self):
        if not self.is_empty():
            temp, self.top = self.top, self.top.next
            temp.next = None
            return temp.value
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.value
        else:
            return None