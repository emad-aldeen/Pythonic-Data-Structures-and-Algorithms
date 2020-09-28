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
                res += f'{current.value} >> '
                current = current.next
            else:
                res = res[:-4]
        else:
            res = 'll is empty!!'
        return res



class Hash_table():
    '''
    using the famous encrypt data way (the hashing):
        inp ---> it only needs the hash table size to create one..
        
        class contains:
            hash: return any inputied key as hashed key
            add: to add the inserted key,value to the hash table
            get: return the value of the inputed key from hash table
            contains: return boolean if the inputed key is already in the hash table
    
    * the class is supported with __str__ methoud to print the hash table
    '''
    def __init__(self, size):
        self.map = [None] * size
        self.size = size


    def hash(self, key):
        '''
        it hashing any inputed key with hash method:
            inp ---> key as int or string
            out >>> the key hashed only in range the hash table size key
        '''
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*77 % self.size


    def add(self, key, value):
        '''
        it used to add your kay and vlaue to the hash table:
            inp ---> key to be saved with own value in tuple
            inp2 ---> value to be saved with own key in tuple

        *** function solve any collision with linked linked list data strusture
        ** used linked list are modfied with functions to handlle only tuples in hash table
        * dont try this on your home!
        '''
        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()
        
        if self.map[hashed_key].includes(key):
        # for dublicate:
            # add to linked list class function to find & replace
            self.map[hashed_key].find_and_replace(key, (key, value))
        else:
            self.map[hashed_key].insert((key, value))


    def get(self, key):
        '''
        it used to get you the value of your inputed key if it exist in the hash table:
            inp ---> key that will search for
            out ---> the value of your inputed key
        
        ** since collision solved by linked list so the used linked list are modfied with functions to handlle only tuples in hash table
        * if key is not exist in the hash table it will return 'null'
        '''
        hashed_key = self.hash(key)

        if self.map[hashed_key]:
            return self.map[hashed_key].get(key)[1]
        return 'null'


    def contains(self, key):
        '''
        your not sure if your key is exist on hash table? this fuction will check and return boolean:
            inp ---> key to be search for
            out >>> boolean if key exist or not

        * since collision solved by linked list so the used linked list are modfied with functions to handlle only tuples in hash table
        '''
        hashed_key = self.hash(key)

        if self.map[hashed_key]:
            return self.map[hashed_key].includes(key)
        return False


    def __str__(self):
        res = ''
        if self.map.count(None) == len(self.map):
            return 'hash table is empty!!'
        for i in range(len(self.map)):
            if self.map[i] != None:
                res += f'in index: {i} : {self.map[i]} \n'
        return res


# if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insert((123, 'hi'), (456, 'not_hi'))
    # print(ll)
    # print(ll.includes(123))
    # print((123, 'hi')[0])

    # test = hash_table(5)
    # test.add('cat', 'hello_TAs')
    # test.add('cat', 'glad to see you guys.. :)')
    # test.add('fatCat', 'how you doin...')
    # test.add('ftaCta', "joy doesn't share food!")
    # print(test.get('fatCat'))
    # print(test.contains('fatCat'))
    # print(test.contains('notFatCat'))
    # print(test)
