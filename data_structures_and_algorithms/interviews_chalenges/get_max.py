from data_structures_and_algorithms.data_structures.stacks_and_queues.node import Node
from data_structures_and_algorithms.data_structures.stacks_and_queues.stack import Stack


def get_max(stack):
    temp_lst = []
    max_val = 0
    while stack.top != None:
        if stack.top.value > max_val:
            max_val = stack.top.value
            temp_lst.append(stack.pop())
        else:
            temp_lst.append(stack.pop())
    while len(temp_lst) > 0:
        stack.push(temp_lst.pop())
    return max_val



if __name__ == "__main__":
    new_stack = Stack()
    new_stack.push(3, 6, 12, 9)
    new_stack.__str__()

    print(get_max(new_stack))
    new_stack.__str__()
