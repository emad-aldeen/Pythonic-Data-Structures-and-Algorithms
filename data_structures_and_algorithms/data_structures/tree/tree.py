class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def is_empty(self):
        """
        method to check if Queue is empty
        """
        if self.front == None:
            return True
        return False


    def enqueue(self, node):
        """
        Method that takes any value as an argument and adds a new node with that value to the back of the queue:
            inp ---> value
        """
        self.length += 1
        new_node = node

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Method that removes the node from the front of the queue, and returns the node’s value:
            out >> the dequeueed value
        """
        if not self.is_empty():
            self.length -= 1
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """
        Method that returns the value of the node located in the front of the queue, without removing it from the queue:
            out >> the front value
        """
        if not self.is_empty():
            return self.front.value
        return None


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, node=None, arr = None):
        """
        Method to return an array of trre values in "pre-order" order:
            out >> list contain tree values in pre-order..
        """
        if arr is None:
            arr = []

        node = node or self.root

        arr.append(node.value)

        if node.left:
            self.pre_order(node.left, arr)

        if node.right:
            self.pre_order(node.right, arr)

        return arr

    def in_order(self, node=None, arr = None):
        """
        Method to return an array of tree values "in-order" :
            out >> list contain tree values in-order..
        """
        if arr is None:
            arr = []

        node = node or self.root

        if node.left:
            self.in_order(node.left, arr)

        arr.append(node.value)

        if node.right:
            self.in_order(node.right, arr)

        return arr

    def post_order(self, node=None, arr = []):
        """
        Method to return an array of tree values "post-order":
            out >> list of tree values in post-order..
        """
        node = node or self.root

        if node.left:
            self.post_order(node.left, arr)

        if node.right:
            self.post_order(node.right, arr)

        arr.append(node.value)

        return arr

    def find_maximum_value(self, root):
        '''
        it used to return the maximum value in the inputd tree:
            out >>> the maximum value in the inputd tree
        '''
        if self.root == None:  
            return float('-inf')

        res = self.root.value 
        left_res = self.find_maximum_value(self.root.left)  
        right_res = self.find_maximum_value(self.root.right) 

        if (left_res > res): 
            res = left_res  

        if (right_res > res):  
            res = right_res  
    
        return res 

    def breadth_first_traversal(self):
        '''
        by level .. it prints evrey level of tree inside an array:
            out >> the tree values sorted by each level by level..
        '''
        res = []
        q = Queue()
        q.enqueue(self.root)
        while q.length > 0:
            cur = q.dequeue()
            res.append(cur.value)
            if cur.left:
                q.enqueue(cur.left)
            if cur.right:
                q.enqueue(cur.right)
        return res
    

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree:
            inp ---> value to be added to binry search tree
        """
        node = Node(value)
        if not self.root:
            self.root = node
            return

        current = self.root
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
        """
        lets cheack if you value is in the tree.. :)
        this method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once:
            inp ---> value to cheack if it is in the tree
            out >> boolean if the value in or not..
        """
        if self.root == None:
            raise "Tree is empty"

        current = self.root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False

    
if __name__ == "__main__":
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

    # print(tree.breadth_first_traversal())
    # print(tree.in_order())