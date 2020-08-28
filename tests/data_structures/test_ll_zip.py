from data_structures_and_algorithms.data_structures.linked_list.linked_list import (
    LinkedList,
)
from data_structures_and_algorithms.data_structures.linked_list.ll_zip.ll_zip import zipLists

def test_zipLists():
    new_list = LinkedList() 
    new_list.insert(3) 
    new_list.insert(2) 
    new_list.insert(1) 
    new_list2 = LinkedList() 
    new_list2.insert(8) 
    new_list2.insert(7) 
    new_list2.insert(6)
    assert zipLists(new_list,new_list2) == "{8} -> {3} -> {7} -> {2} -> {6} -> {1} -> NULL"
