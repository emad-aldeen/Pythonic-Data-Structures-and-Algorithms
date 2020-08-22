class Node:
    '''
    the 'Node' class it will create new node
        input --> the node value
    by defult `node.next` will point to 'None'
    '''
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
    """
    creating new linked lists:
        def insert ---> input --> the node to insert to linked list
        def includes ---> input --> the vlaue you want to search for >> output >> boleen
        def toString >> output >> your linked list by format '{ val } -> '
    """
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node

    def includes(self,num):
        current = self.head
        while current:
            if current.value == num:
                return True
            current = current.next
        return False
    

    def toString(self):
        result = ""
        current = self.head
        while current:
            result += f'{ {current.value} } -> '
            current = current.next
        result += 'NULL'
        return result


if __name__ == '__main__':
    mainll = LinkedList()
    mainll.insert(1)
    mainll.insert(6)
    mainll.insert(9)
    print(mainll.includes(5))
    print(mainll.toString())
    empty = LinkedList()
    print(empty.toString())
    print(mainll.head.value)
