class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            temp = self.top
            new_node.next = temp
            self.top = new_node

    def pop(self):
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
        try:
            return self.top.value
        except AttributeError:
            return "stack is empty!"


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