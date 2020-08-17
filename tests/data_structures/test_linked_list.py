from data_structures.linked_list.linked_list import (
    LinkedList,
)


def test_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)
