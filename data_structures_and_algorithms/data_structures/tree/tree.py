class _Node:
    """Private class to create a nodes for the tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    """class Queue which implements Queue data structure with its common methods"""

    def __init__(self):
        """Initiate class"""

        self.front = None
        self.rear = None

    def is_empty(self):
        """method to check if Queue is empty"""

        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        """Method that takes any value as an argument and adds a new node with that value to the back of the queue """

        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """Method that removes the node from the front of the queue, and returns the node’s value."""

        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """Method that returns the value of the node located in the front of the queue, without removing it from the queue."""

        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    """Class to create a binary tree"""
    def __init__(self):
        self._root = None

    def pre_order(self, node=None, arr = None):
        """Method to return an array of trre values in "pre-order" order"""

        if arr is None:
            arr = []

        node = node or self._root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr = None):
        """Method to return an array of tree values "in-order" """
        if arr is None:
            arr = []

        node = node or self._root

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)

        return arr

    def post_order(self, node=None, arr = []):
        """Method to return an array of tree values "post-order" """

        node = node or self._root

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr

    @staticmethod
    def breadth_first(tree, node = None, array = None):
        """ A static method which takes a Binary Tree as its unique input, traversing the input tree using a Breadth-first approach, and returns a list of the values in the tree in the order they were encountered."""

        q = Queue()
        if array is None:
            array = []
        if tree._root:
            q.enqueue(tree._root)

        while q.peek():
            node_front = q.dequeue()
            array.append(node_front.value)

            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)

        return array


class BinarySearchTree(BinaryTree):
    """Class to create a Binary Search Tree """

    def add(self, value):
        """Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree"""

        node = _Node(value)
        if not self._root:
            self._root = node
            return

        current = self._root
        while True:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return


    def contains(self,value):
        """Method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once."""

        if self._root == None:
            raise myException("Tree is empty")

        current = self._root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False

class myException(Exception):
    pass

