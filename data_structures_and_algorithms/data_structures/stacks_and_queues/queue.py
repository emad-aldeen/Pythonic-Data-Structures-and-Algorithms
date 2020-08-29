from data_structures_and_algorithms.data_structures.stacks_and_queues.node import Node

class Queue():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *value):
        '''
        used to add nodes to rear of the queue:
            input ---> value to create node from it then add to the queue..
        '''
        for i in value:
            new_node = Node(i)
            if self.front == None and self.rear == None:
                self.front = new_node
                self.rear = new_node
            else:
                temp = self.rear
                self.rear = new_node
                temp.next = new_node


    def dequeue(self):
        '''
        it only pop the first node in the front of the queue..
        '''
        try:
            self.front.value
        except AttributeError:
            return "this queue is empty!!"
        else:
            temp = self.front
            temp2 = temp.next
            self.front = temp2
            return temp.value

    def peek(self):
        '''
        return the first node value of the front of the queue:
            output >> the front value of the queue
        '''
        try:
            return self.front.value
        except AttributeError:
            return "this queue is empty!!"


    def isEmpty(self):
        '''
        cheak if the queue is empty or not:
            output >> boleen
        '''
        if self.front == None and self.rear == None:
            return True
        else:
            return False
 




if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)
    print(queue.front.value)
    queue.enqueue(7)
    # print(queue.rear.value)
    queue.enqueue(9)
    print(queue.rear.value)
    print (queue.dequeue())
    print(queue.front.value)
    print (queue.peek())
    not_queue = Queue()
    print(not_queue.peek())
    print(queue.isEmpty())
    print(not_queue.isEmpty())