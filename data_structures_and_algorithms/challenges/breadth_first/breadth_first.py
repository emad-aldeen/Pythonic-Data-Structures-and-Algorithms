from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

def breadth_first_traversal(root): 
    '''
    function which takes a Binary Tree root as its unique input and returns a list of the values in the tree in the order they were encountered:
        inp ---> the root of the inputed tree
        out >>> a list of the values in the tree in the order they were encountered
    '''
    breadth, result = [], []
    
    if root:
        result.append(root)
    while len(result) > 0:
        current = result.pop(0)
        breadth.append(current.value)
        if current.left:
            result.append(current.left)
        if current.right:
            result.append(current.right)
            
    return breadth



