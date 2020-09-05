from data_structures_and_algorithms.data_structures.tree.tree import _Node, BinaryTree, BinarySearchTree, Queue
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
    assert tree._root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree._root.value == 'apples'

def test_add_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree._root.value == 10
    assert tree._root.left.value == 5
    assert tree._root.right.value == 15

def test_add_more_members_for_balanced():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(25)
    tree.add(60)
    tree.add(23)

    assert tree._root.value == 15
    assert tree._root.left.value == 11
    assert tree._root.right.value == 25
    assert tree._root.left.left.value == 7
    assert tree._root.left.right.value == 13
    assert tree._root.right.right.value == 60
    assert tree._root.right.left.value == 23

def test_add_more_members_for_imbalanced(my_bst):

    assert my_bst._root.value == 15
    assert my_bst._root.left.value == 11
    assert my_bst._root.left.right.value == 13
    assert my_bst._root.left.left.value == 7
    assert my_bst._root.left.left.left.value == 5
    assert my_bst._root.left.left.right.value == 8

def test_add_one_node():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree._root.value == 20
    assert tree._root.left == None
    assert tree._root.right == None


def test_check_one_node_tree():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree.contains(20) == True
    assert tree.contains(21) == False


def test_contains_true(my_bst):

    assert my_bst._root.value == 15
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


def test_breadth_first_binarysearch(my_bst):
   assert BinaryTree.breadth_first(my_bst) == [15, 11, 19, 7, 13, 17, 23, 5, 8]

def test_breadth_first_binarytree_empty():
    tree = BinaryTree()
    assert BinaryTree.breadth_first(tree) == []

def test_breadth_first_binarytree_one_element():
    tree = BinaryTree()
    tree._root = _Node(8)
    assert BinaryTree.breadth_first(tree) == [8]

def test_breadth_first_binarytree_with_letters():
    tree = BinaryTree()
    tree._root = _Node(8)
    tree._root.left = _Node("a")
    tree._root.right = _Node(-2)
    assert BinaryTree.breadth_first(tree) == [8, "a", -2]
    tree._root.left.left = _Node(195)
    tree._root.left.right = _Node("cat")
    tree._root.right.right = _Node(8)
    tree._root.left.left.left = _Node(-0.56)
    tree._root.left.left.right = _Node(9)
    tree._root.right.right.right = _Node(23)
    tree._root.right.right.right.left = _Node([5, 7])
    assert BinaryTree.breadth_first(tree) == [8, "a", -2, 195,"cat", 8, -0.56, 9, 23, [5,7]]


