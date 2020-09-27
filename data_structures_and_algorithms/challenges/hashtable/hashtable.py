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
    """
    def __init__(self):
        self.head = None
    

    def insert(self, value=None):
        '''
        insert new node to linked list:
            input ---> the vlaue you want to added to linked list
            * if there is no value it will raise 'ValueError'
        '''
        if value is None:
            raise Exception('Please insert vlaue as argument')
        else:
            new_node = Node(value)

            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next

                current.next = new_node


    def includes(self, value=None):
        '''
        function designed to search in your linked list for the input value:
            input ---> value you want to search for..
            output >> boleen if your input exist in the ll
            * none input will raise ValueError..
        '''
        if value is None:
            raise Exception('Please insert vlaue as argument')
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False

    def __str__(self):
        if self.head:
            res = ''
            current = self.head
            while current:
                res += f'{ {current.value} } >> '
                current = current.next
        else:
            res = 'll is empty!!'
        return res

class hash_table():
    def __init__(self, size):
        self.map = [None] * size
        self.size = size
    
    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*77 % self.size

    def add(self, key, value):
        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()

        self.map[hashed_key].insert((key, value))