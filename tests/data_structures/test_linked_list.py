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
    except TypeError:
        raise Exception('There has been an error in the system')


def test_append():
    ll.append(11)
    current = ll.head
    while current.next:
        current = current.next
    assert current.next == None
    assert current.value == 11
    assert ll.toString() == '{3} -> {6} -> {9} -> {11} -> NULL'


def test_insertBefore():
    ll.insertBefore(3, 2)
    ll.insertBefore(9, 5)
    actual = ll.toString()
    expected =  '{2} -> {3} -> {6} -> {5} -> {9} -> {11} -> NULL'
    assert actual == expected

def test_insertBefore_edgeCase():
    ll.insertBefore(12, 4)
    assert "this node is not exist!"


def test_insertAfter():
    ll.insertAfter(9, 10)
    ll.insertAfter(11, 12)
    actual = ll.toString()
    expected =  '{2} -> {3} -> {6} -> {5} -> {9} -> {10} -> {11} -> {12} -> NULL'
    assert actual == expected

def test_insertAfter_edgeCase():
    ll.insertAfter(1, 10)
    assert "this node is not exist!"


def test_delete_node():
    ll.delete_node(12)
    ll.delete_node(11)
    ll.delete_node(10)
    ll.delete_node(5)
    assert ll.toString() == '{2} -> {3} -> {6} -> {9} -> NULL'
    ll.delete_node(2)
    assert ll.toString() == '{3} -> {6} -> {9} -> NULL'