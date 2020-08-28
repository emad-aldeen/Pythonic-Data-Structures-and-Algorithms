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



if __name__ == '__main__':
    stack = Stack()
    stack.push(7)
    stack.push(9)
    stack.push(12)
    print (stack.top.value)
    print (stack.top.next.value)
