class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.max_val = 0
    
    def push(self, *value):
        '''
        used to add nodes to top of the stack:
            input ---> value to create node from it then add to the top of the stack..
        '''
        for i in value:
            new_node = Node(i)

            if i > self.max_val:
                self.max_val = i

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
            

    def __str__(self):
        result = ''
        current = self.top
        while current:
            result += f"{{{current.value}}} -> "
            current = current.next
        print(result)


    def get_max(self):
        return self.max_val

        # temp_lst = []
        # max_val = 0
        # while stack.top != None:
        #     if stack.top.value > max_val:
        #         max_val = stack.top.value
        #         temp_lst.append(stack.pop())
        #     else:
        #         temp_lst.append(stack.pop())
        # while len(temp_lst) > 0:
        #     stack.push(temp_lst.pop())
        # return max_val



if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push(3, 6, 12, 9)
    new_stack.__str__()

    print(new_stack.get_max())
    new_stack.__str__()
