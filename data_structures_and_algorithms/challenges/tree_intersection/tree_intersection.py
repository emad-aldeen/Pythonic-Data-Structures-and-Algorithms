from data_structures_and_algorithms.data_structures.tree.tree import BinarySearchTree, BinaryTree, Node

def tree_intersection(tree1, tree2):
    '''
    function designed by using breadth_first_traversal in trees it will get you the same leaf in both trees:
        inp ---> tree1
        inp2 ---> tree2
        out >>> list with Similar leafes in both trees
    '''
    res = []
    cont1 = tree1.breadth_first_traversal()
    cont2 = tree2.breadth_first_traversal()
    for i in range(len(cont1)):
        if cont1[i] == cont2[i]:
            res.append(cont1[i])
    if len(res) > 0:
        return res
    else:
        return None

