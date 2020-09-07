from data_structures_and_algorithms.data_structures.tree.tree import _Node, Queue, BinaryTree

def breadth_first_traversal(root): 
    breadth, output = [], []
    if not root:
        return 'tree empty!!'
    else:
        if root:
            output.append(root)
        while output:
            current = output.pop(0)
            breadth.append(current.value)
            if current.left:
                output.append(current.left)
            if current.right:
                output.append(current.right)
    return breadth



