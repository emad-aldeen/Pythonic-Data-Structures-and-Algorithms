from data_structures_and_algorithms.challenges.tree_intersection.tree_intersection import tree_intersection
from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree, BinarySearchTree, Node

def test_same_tree_type():
    tree1 = BinaryTree()
    tree1.root = Node(5)
    tree1.root.right = Node(6)
    tree1.root.left = Node(4)
    tree1.root.right.right = Node(7)
    tree1.root.right.left = Node(5)
    tree1.root.left.left = Node(2)
    tree1.root.left.right = Node(4)
    tree2 = BinaryTree()
    tree2.root = Node(4)
    tree2.root.right = Node(6)
    tree2.root.right.right = Node(7)
    tree2.root.right.left = Node(5)
    tree2.root.left = Node(3)
    tree2.root.left.right = Node(3)
    tree2.root.left.left = Node(2)
    actual = tree_intersection(tree1, tree2)
    expected = [6,2,5,7]
    assert actual == expected


def test_difrent_tree_type():
    tree3 = BinaryTree()
    tree3.root = Node(5)
    tree3.root.right = Node(6)
    tree3.root.left = Node(4)
    tree3.root.right.right = Node(7)
    tree3.root.right.left = Node(5)
    tree3.root.left.left = Node(2)
    tree3.root.left.right = Node(4)
    tree4 = BinarySearchTree()
    tree4.add(4)
    tree4.add(6)
    tree4.add(7)
    tree4.add(5)
    tree4.add(3)
    tree4.add(3)
    tree4.add(2)
    actual = tree_intersection(tree3, tree4)
    expected = [6,2,5,7]
    assert actual == expected
    

def test_no_similar_leafs():
    tree5 = BinarySearchTree()
    tree5.add(4)
    tree5.add(6)
    tree5.add(7)
    tree5.add(5)
    tree5.add(3)
    tree5.add(3)
    tree5.add(2)
    tree6 = BinarySearchTree()
    tree6.add(6)
    tree6.add(5)
    tree6.add(1)
    tree6.add(45)
    tree6.add(10)
    tree6.add(16)
    tree6.add(5)
    assert tree_intersection(tree5, tree6) == None


def test_tow_same_tree():
    tree7 = BinarySearchTree()
    tree7.add(6)
    tree7.add(5)
    tree7.add(1)
    tree7.add(45)
    tree7.add(10)
    tree7.add(16)
    tree7.add(5)
    tree8 = BinarySearchTree()
    tree8.add(6)
    tree8.add(5)
    tree8.add(1)
    tree8.add(45)
    tree8.add(10)
    tree8.add(16)
    tree8.add(5)
    assert tree_intersection(tree7, tree8) == [6, 5, 45, 1, 5, 10, 16]