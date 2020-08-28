from data_structures_and_algorithms.data_structures.stacks_and_queues.stack import (Stack)

def test_push():
    stack = Stack()
    stack.push(3)
    expected = stack.top.value
    assert expected == 3


def test_pop():
    stack = Stack()
    stack.push(3)
    expected = stack.pop()
    assert expected == 3
    not_stack = Stack()
    assert not_stack.pop() == "stack is empty!"


def test_peek():
    stack = Stack()
    stack.push(3)
    expected = stack.peek()
    assert expected == 3
    not_stack = Stack()
    assert not_stack.peek() == "stack is empty!"


def test_is_empty():
    stack = Stack()
    stack.push(3)
    expected = stack.is_empty()
    assert expected == False
    not_stack = Stack()
    assert not_stack.is_empty() == True

