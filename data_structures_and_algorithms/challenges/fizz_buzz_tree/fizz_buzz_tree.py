from data_structures_and_algorithms.data_structures.tree.tree import BinaryTree


def fizz_buzz(value):
    """
    Function to do the fizz_buzz on the given value:
        inp ---> value to be checked if fizz , buzz OR fizzbuzz
        out >>> string fizz , buzz OR fizzbuzz
    """
    if value % 15 == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
    else:
        return str(value)


def fizz_buzz_tree(tree):
    """
    Function to change all values in the given tree according to fizz_buzz:
        inp ---> tree to be checked..
        out >>> new tree with fizz - buzz or the same number if it not..
    """
    new_tree = BinaryTree()
    if not tree.root:
        return new_tree

    def helper(current):
        """
        Helper function to use in recurtion to add new values in the new_tree according to their positions in the original tree
        """
        node = _Node(fizz_buzz(current.value))
        if current.left:
            node.left = helper(current.left)
        if current.right:
            node.right = helper(current.right)
        return node
    new_tree.root = helper(tree.root)

    return new_tree
