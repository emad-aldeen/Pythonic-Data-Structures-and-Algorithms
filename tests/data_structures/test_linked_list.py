from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
import pytest


ll = LinkedList()
ll.insert(3)
ll.insert(6)
ll.insert(9)

def test_instance():
    assert isinstance(ll, LinkedList)

def test_insert():
    result = ''
    linked_list = ll.head
    while linked_list:
        result += f'{linked_list.value},'
        linked_list = linked_list.next
    assert result == '3,6,9,'

def test_head():
    assert ll.head.value == 3

def test_finding_notExist_value():
    assert ll.includes(5) == False

def test_finding_exist_value():
    assert ll.includes(6) == True

def test_string_str():
    assert ll.toString() == '{3} -> {6} -> {9} -> NULL'

@pytest.mark.skip(reason='Testing Erorr')
def test_Erorr():
    try:
        ll.insert()
    except:
        raise Exception('There has been an error in the system')