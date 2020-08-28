from data_structures_and_algorithms.data_structures.stacks_and_queues.node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.front == None and self.rear == None:
            self.front = new_node
            self.rear = new_node
        else:
            temp = self.rear
            self.rear = new_node
            temp.next = new_node

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    print(queue.front.value)
    queue.enqueue(7)
    # print(queue.rear.value)
    queue.enqueue(9)
    print(queue.rear.value)