from data_structures_and_algorithms.challenges.find_maximum_binary_tree.find_maximum_binary_tree import _Node, find_maximum_value

def test_find_maximum_value1():
    root = _Node(7)
    root.left = _Node(7)
    root.right = _Node(5)
    root.left.left = _Node(2)
    root.left.right = _Node(6)
    root.left.right.left = _Node(5)
    root.left.right.right = _Node(11)
    root.right.right = _Node(9)
    root.right.right.left = _Node(4)

    assert find_maximum_value(root) == 11

    
def test_find_maximum_value2():
    root = _Node(9)
    root.left = _Node(16)
    root.right = _Node(12)
    
    actual = find_maximum_value(root)
    expected = 16

    assert actual == expected


def test_find_maximum_value3():
    root = _Node(1)

    assert find_maximum_value(root) == 1

