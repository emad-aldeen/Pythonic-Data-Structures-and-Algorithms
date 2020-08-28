from data_structures_and_algorithms.data_structures.stacks_and_queues.queue import Queue

def test_queue():
    queue = Queue()
    queue.enqueue(5)
    expected = queue.front.value
    assert expected == 5
    queue.enqueue(7)
    # print(queue.rear.value)
    queue.enqueue(9)
    assert queue.rear.value == 9


def test_dequeue():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    assert queue.rear.value == 9
    expected = queue.dequeue()
    assert expected == 5
    assert queue.rear.value == 9
    assert queue.front.value == 7
    assert queue.dequeue() == 7
    assert queue.rear.value == 9
    assert queue.front.value == 9


def test_peek():
    queue = Queue()
    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)
    assert queue.peek() == 5
    not_queue = Queue()
    assert not_queue.peek() == 'this queue is empty!!'


