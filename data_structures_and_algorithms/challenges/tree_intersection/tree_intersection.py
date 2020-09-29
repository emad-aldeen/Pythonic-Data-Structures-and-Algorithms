from data_structures_and_algorithms.data_structures.tree.tree import BinarySearchTree, BinaryTree, Node

def tree_intersection(tree1, tree2, res=[]):
    '''
    function designed by using breadth_first_traversal in trees it will get you the same leaf in both trees:
        inp ---> tree1
        inp2 ---> tree2
        out >>> list with Similar leafes in both trees
    '''
    cont1 = tree1.breadth_first_traversal()
    cont2 = tree2.breadth_first_traversal()
    for i in range(len(cont1)):
        if cont1[i] == cont2[i]:
            res.append(cont1[i])
    if len(res) > 0:
        return res
    else:
        return None


# if __name__ == '__main__':
#     tree1 = BinaryTree()
#     tree1.root = Node(5)
#     tree1.root.right = Node(6)
#     tree1.root.left = Node(4)
#     tree1.root.right.right = Node(7)
#     tree1.root.right.left = Node(5)
#     tree1.root.left.left = Node(2)
#     tree1.root.left.right = Node(4)
#     tree2 = BinarySearchTree()
#     tree2.add(4)
#     tree2.add(6)
#     tree2.add(7)
#     tree2.add(5)
#     tree2.add(3)
#     tree2.add(3)
#     tree2.add(2)
#     # print(tree_intersection(tree1, tree2))
#     print(tree2.breadth_first_traversal())