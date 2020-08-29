from data_structures_and_algorithms.data_structures.stacks_and_queues.node import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, *value):
        '''
        used to add nodes to top of the stack:
            input ---> value to create node from it then add to the top of the stack..
        '''
        for i in value:
            new_node = Node(i)
            if self.top == None:
                self.top = new_node
            else:
                temp = self.top
                new_node.next = temp
                self.top = new_node

    def pop(self):
        '''
        it only pop the first node in the top of the stack..
        '''
        try:
            self.top.value
        except AttributeError:
            return "stack is empty!"
        else:
            result = self.top.value
            temp = self.top.next
            self.top = temp
            return result

    def peek(self):
        '''
        return the first node value of the top of the stack:
            output >> the top value of the stack
        '''
        try:
            return self.top.value
        except AttributeError:
            return "stack is empty!"


    def is_empty(self):
        '''
        cheak if the stack is empty or not:
            output >> boleen
        '''
        if self.top:
            return False
        else:
            return True







if __name__ == '__main__':
    stack = Stack()
    stack.push(7)
    stack.push(9)
    stack.push(12)
    print (stack.top.value)
    print (stack.top.next.value)
    stack.pop()
    print (stack.top.value)
    not_stack = Stack()
    print(not_stack.pop())
    print (stack.peek())
    print (not_stack.peek())

    print (stack.is_empty())
    print (not_stack.is_empty())