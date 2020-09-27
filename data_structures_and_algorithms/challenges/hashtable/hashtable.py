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
    

    def insert(self, *value):
        '''
        insert new node to linked list:
            input ---> the vlaue you want to added to linked list
            * if there is no value it will raise 'ValueError'
        '''
        if value is None:
            raise Exception('Please insert vlaue as argument')
        else:
            for i in value:
                new_node = Node(i)

                if not self.head:
                    self.head = new_node
                else:
                    current = self.head
                    while current.next:
                        current = current.next

                    current.next = new_node


    def includes(self, value):
        '''
        function designed to search in your linked list for the input value:
            input ---> value you want to search for..
            output >> boleen if your input exist in the ll
            ** this function only to handle tuples of tow elemnts
            * none input will raise ValueError..
        '''
        if value is None:
            raise Exception('Please insert value as argument!!')
        else:
            current = self.head
            while current:
                if current.value[0] == value:
                    return True
                current = current.next
            return False


    def find_and_replace(self, value, value2):
        '''
        function designed to search in your linked list for the input value then replace it with the second value2:
            input ---> value you want to be replaced..
            input2 ---> value2 you want to replace with
            * this function only to handle tuples of tow elemnts
            ** None any of inputs will raise ValueError..
        '''
        if value is None or value2 is None:
            raise Exception('Please insert both values as argument!!')
        else:
            current = self.head
            while current:
                if current.value[0] == value:
                    current.value = value2
                    return
                current = current.next


    def get(self, value):
        '''
        function designed to search in your linked list for the input value then return it:
            input ---> value you want to search for..
            output >> tuple contains the value you want
            * this function only to handle tuples of tow elemnts
            ** None input will raise ValueError..
        '''
        if value is None:
            raise Exception('Please insert value as argument!')
        else:
            current = self.head
            while current:
                if current.value[0] == value:
                    return current.value
                current = current.next


    def __str__(self):
        if self.head:
            res = ''
            current = self.head
            while current:
                res += f'{ {current.value} } >> '
                current = current.next
            else:
                res = res[:-4]
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
        
        if self.map[hashed_key].includes(key):
        # for dublicate:
            # add to linked list class function to find & replace
            self.map[hashed_key].find_and_replace(key, (key, value))
        else:
            self.map[hashed_key].insert((key, value))


    def __str__(self):
        res = ''
        for i in range(len(self.map)):
            if self.map[i] != None:
                res += f'in index: {i} : {self.map[i]} \n'
        return res


if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insert((123, 'hi'), (456, 'not_hi'))
    # print(ll)
    # print(ll.includes(123))
    # print((123, 'hi')[0])

    test = hash_table(5)
    test.add('cat', 'hello_TAs')
    test.add('cat', 'glad to see you guys.. :)')
    print(test)
