from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, BinarySearchTree, Queue
import pytest

@pytest.fixture
def my_bst():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(8)
    tree.add(5)
    tree.add(19)
    tree.add(17)
    tree.add(23)


    return tree

def test_tree_instance():
    tree = BinaryTree()
    assert tree.root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree.root.value == 'apples'

def test_add_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.value == 10
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

def test_add_more_members_for_balanced():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(25)
    tree.add(60)
    tree.add(23)

    assert tree.root.value == 15
    assert tree.root.left.value == 11
    assert tree.root.right.value == 25
    assert tree.root.left.left.value == 7
    assert tree.root.left.right.value == 13
    assert tree.root.right.right.value == 60
    assert tree.root.right.left.value == 23

def test_add_more_members_for_imbalanced(my_bst):

    assert my_bst.root.value == 15
    assert my_bst.root.left.value == 11
    assert my_bst.root.left.right.value == 13
    assert my_bst.root.left.left.value == 7
    assert my_bst.root.left.left.left.value == 5
    assert my_bst.root.left.left.right.value == 8

def test_add_one_node():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree.root.value == 20
    assert tree.root.left == None
    assert tree.root.right == None


def test_check_one_node_tree():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree.contains(20) == True
    assert tree.contains(21) == False


def test_contains_true(my_bst):

    assert my_bst.root.value == 15
    assert my_bst.contains(7) == True
    assert my_bst.contains(9) == False

def test_pre_order(my_bst):
    assert my_bst.pre_order() == [15, 11, 7, 5, 8, 13, 19, 17, 23]

def test_pre_order_one():
    tree_one = BinarySearchTree()
    tree_one.add(20)
    assert tree_one.pre_order() == [20]

def test_in_order(my_bst):
    assert my_bst.in_order() == [5, 7, 8, 11, 13, 15, 17, 19, 23]

def test_post_order(my_bst):
    assert my_bst.post_order() == [5, 8, 7, 13, 11, 17, 23, 19, 15]




