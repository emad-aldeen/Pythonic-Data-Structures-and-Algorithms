from data_structures_and_algorithms.data_structures.stacks_and_queues.stack import Stack

class PseudoQueue:
    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()
        self.count = 0
    

    def enqueue(self, *value):
        '''
        used to add new values (nodes) to your 'PseudoQueue':
            inputs --> values to add
        '''
        self.count += 1
        for i in value:
            self.first_stack.push(i)

    def dequeue(self):
        '''
        it used to return the first vlaue(node) in your 'PseudoQueue', first pushed:
        '''
        if self.second_stack.is_empty():
            while self.count > 0:
                self.second_stack.push(self.first_stack.pop())
                self.count-=1
            result = self.second_stack.pop()
            while True:
                self.first_stack.push(self.second_stack.pop())
                self.count +=1
                if self.second_stack.is_empty():
                    return result
        else:
            return "stack is empty!"


    def __str__(self):
        result = ''
        if self.first_stack.is_empty():
            current = self.second_stack.top
        else:
            current = self.first_stack.top
        while current:
            result += f"{{{current.value}}} -> "
            current = current.next
        return result




new_psQ = PseudoQueue()
new_psQ.enqueue(3)
new_psQ.enqueue(6)
new_psQ.enqueue(9)
new_psQ.enqueue(4)
new_psQ.enqueue(7)
new_psQ.enqueue(10)

print(new_psQ.__str__())
def test_dequeue():
    assert new_psQ.dequeue() == 3
    # print(new_psQ.__str__())
    assert new_psQ.dequeue() == 6
    # print(new_psQ.__str__())
    assert new_psQ.dequeue() == 9
    # print(new_psQ.__str__())

if __name__ == "__main__":
    test_dequeue()
    print(new_psQ.__str__())