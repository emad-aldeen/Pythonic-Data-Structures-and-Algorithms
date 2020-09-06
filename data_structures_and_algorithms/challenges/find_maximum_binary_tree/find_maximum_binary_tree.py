from data_structures_and_algorithms.data_structures.tree.tree import _Node


def find_maximum_value(root):
    '''
    it used to return the maximum value in the inputd tree:
        inp ---> the root of the tree you want to search in.., it will also re used in recursev way as root for dub tree..
        out >>> the maximum value in the inputd tree
    '''
    if root == None:  
        return float('-inf')

    res = root.value 
    left_res = find_maximum_value(root.left)  
    right_res = find_maximum_value(root.right) 

    if (left_res > res): 
        res = left_res  

    if (right_res > res):  
        res = right_res  
 
    return res 



# if __name__ == '__main__': 
#     root = _Node(7)
#     root.left = _Node(7)
#     root.right = _Node(5)
#     root.left.left = _Node(2)
#     root.left.right = _Node(6)
#     root.left.right.left = _Node(5)
#     root.left.right.right = _Node(11)
#     root.right.right = _Node(9)
#     root.right.right.left = _Node(4)
  
#     print("Maximum element is", find_maximum_value(root)) 