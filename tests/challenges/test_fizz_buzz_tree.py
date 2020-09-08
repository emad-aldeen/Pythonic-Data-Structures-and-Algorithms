from data_structures_and_algorithms.challenges.fizz_buzz_tree.fizz_buzz_tree import fizz_buzz, fizz_buzz_tree
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, _Node
from data_structures_and_algorithms.challenges.breadth_first.breadth_first import breadth_first_traversal
import pytest

def test_fizz_buzz_tree():
    bt = BinaryTree()
    bt.root = _Node(2)
    bt.root.left = _Node(7)
    bt.root.right = _Node(5)
    bt.root.left.left = _Node(2)
    bt.root.left.right = _Node(6)
    bt.root.right.right = _Node(9)
    bt.root.right.right.left = _Node(4)
    bt.root.left.right.right = _Node(11)
    bt.root.left.right.left = _Node(15)

    new = fizz_buzz_tree(bt)
    assert breadth_first_traversal(new.root) == ['2', '7', 'Buzz', '2', 'Fizz', 'Fizz', 'FizzBuzz', '11', '4']

   

def test_tree_with_minus():
    test = BinaryTree()
    test.root = _Node(-2)
    test.root.left = _Node(-7)
    test.root.right = _Node(-5)
    test.root.left.left = _Node(-2)
    test.root.left.right = _Node(-6)
    test.root.right.right = _Node(-9)
    test.root.right.right.left = _Node(-4)
    test.root.left.right.right = _Node(-15)
    test.root.left.right.left = _Node(0)
    
    expected = ['-2', '-7', 'Buzz', '-2', 'Fizz', 'Fizz', 'FizzBuzz', 'FizzBuzz', '-4']
    actual = breadth_first_traversal(fizz_buzz_tree(test).root)

    assert expected == actual


def test_tree_with_one_value():
    test = BinaryTree()
    test.root = _Node(5)
    
    expected = ['Buzz']
    actual = breadth_first_traversal(fizz_buzz_tree(test).root)
    
    assert expected == actual

def test_error():
    test = 'not tree'
    with pytest.raises(ValueError):
        fizz_buzz_tree(test)