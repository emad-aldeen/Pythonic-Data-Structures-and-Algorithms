from data_structures_and_algorithms.challenges.queue_with_stacks.queue_with_stacks import PseudoQueue

def test_PseudoQueue():
    new_psQ = PseudoQueue()
    assert new_psQ.__str__() == ''

def test_PseudoQueue_enqueue():
    new_psQ = PseudoQueue()
    new_psQ.enqueue(3)
    new_psQ.enqueue(6)
    new_psQ.enqueue(9)
    new_psQ.enqueue(4)
    new_psQ.enqueue(7)
    new_psQ.enqueue(10)
    assert new_psQ.__str__() == '{10} -> {7} -> {4} -> {9} -> {6} -> {3} -> '

def test_PseudoQueue_enqueue_multi():
    new_psQ = PseudoQueue()
    new_psQ.enqueue(3, 6, 9, 4, 7, 10)
    assert new_psQ.__str__() == '{10} -> {7} -> {4} -> {9} -> {6} -> {3} -> '

def test_PseudoQueue_dequeue():
    new_psQ = PseudoQueue()
    new_psQ.enqueue(3)
    new_psQ.enqueue(6)
    new_psQ.enqueue(9)
    new_psQ.enqueue(4)
    new_psQ.enqueue(7)
    new_psQ.enqueue(10)
    assert new_psQ.dequeue() == 3


def test_PseudoQueue_dequeue_multi():
    new_psQ = PseudoQueue()
    new_psQ.enqueue(3)
    new_psQ.enqueue(6)
    new_psQ.enqueue(9)
    new_psQ.enqueue(4)
    new_psQ.enqueue(7)
    new_psQ.enqueue(10)
    new_psQ.dequeue()
    new_psQ.dequeue()
    new_psQ.dequeue()
    assert new_psQ.__str__() == '{10} -> {7} -> {4} -> '



def test_PseudoQueue_dequeue_faliure_case():
    new_psQ = PseudoQueue()
    assert new_psQ.dequeue() == "stack is empty!"