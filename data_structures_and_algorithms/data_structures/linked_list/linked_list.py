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
        def append ---> input ---> it will append it in the end of the linked list
        def insertBefore ---> input1, input2 ---> the value you want to insert before then the new value >> output >> confirmation message if printed..
        def insertAfter ---> input1, input2 ---> the value you want to insert after then the new value >> output >> confirmation message if printed..
        def delete_node ---> input ---> the value you want to delete
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
    

    def toString(self):
        '''
        lets print your linked list by format '{nodeValue} -> '... :)
        '''
        result = ""
        current = self.head
        while current:
            result += f'{ {current.value} } -> '
            current = current.next
        result += 'NULL'
        return result


    def append(self, value):
        '''
        append new node to your linked list:
            input ---> value you want to append
            output >> if you print this methoud it will output confirmation message..
        '''
        new_node = Node(value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def insertBefore(self, value, newVal):
        '''
        function used to add new node you input it value(second argument) before the first argument you inputed..
            input ---> value you want to insertBefore it the next input
            input2 ---> the value of the new node you want to insert
            output ---> if you printed this method it will returen to you confirmation messege
            * if the node not exist it will return faill messege
        '''
        new_node = Node(newVal)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            if self.head.value == value:
                old_node = self.head
                self.head = new_node
                new_node.next = old_node
                return f'secssfuly added "{newVal}" to the linked list..'
            else:
                current = self.head
            while current.next != None:
                if current.next.value == value:
                    old_node = current.next
                    current.next = new_node
                    new_node.next = old_node
                    return f'secssfuly added "{newVal}" to the linked list..'
                else:
                    current = current.next

            return "this node is not exist!"

            # while True:
            #     try:
            #         current.next.value
            #     except AttributeError:
            #         return "this node is not exist!"
            #     else:
            #         if current.next.value != value:
            #             current = current.next
            #             continue
            #     break

            # old_node = current.next
            # current.next = new_node
            # new_node.next = old_node
            # return f'secssfuly added "{newVal}" to the linked list..'



    def insertAfter(self, value, newVal):
        '''
        function used to add new node you input it value(second argument) after the first argument you inputed..
            input ---> value you want to insertAfter the next input
            input2 ---> the value of the new node you want to insert
            output ---> if you printed this method it will returen to you confirmation messege
            * if the node not exist it will return faill messege
        '''
        new_node = Node(newVal)
        current = self.head
        if not self.head:
                self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    current = current.next
                    old_node = current.next
                    current.next = new_node
                    new_node.next = old_node
                    return f'secssfuly added "{newVal}" to the linked list..'
                else:
                    current = current.next
                    
            return "this node is not exist!"

    
    def delete_node(self, value):
        '''
        want to delete_node?
        this function is the solution to delete node you want from your linked list:
            input ---> value you want to delete
        '''
        if self.head.value == value:
            self.head = self.head.next
            return "done!"
        else:
            current = self.head
            while current:
                if current.next.value == value:
                    current.next = current.next.next
                    return "done!"
                current = current.next


if __name__ == '__main__':
    mainll = LinkedList()
    mainll.insert(3)
    mainll.insert(6)
    mainll.insert(9)
    print(mainll.includes(5))
    print(mainll.toString())
    empty = LinkedList()
    print(empty.toString())
    print(mainll.head.value)
    print(mainll.insertBefore(2, 4))
    print(mainll.toString())
    print(mainll.insertBefore(6, 4))
    print(mainll.toString())
    print(mainll.insertBefore(3, 2))
    print(mainll.toString())

    print(mainll.insertAfter(5, 4))
    print(mainll.toString())
    print(mainll.insertAfter(6, 1))
    print(mainll.toString())

    print(mainll.delete_node(3))
    print(mainll.toString())