from data_structures_and_algorithms.data_structures.stacks_and_queues.node import Node

class Animal():
    def __init__(self, type):
        self.type = type
        self.next = None

class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None
     

    def enqueue(self, animal):
        if self.front == None and self.rear == None:
            self.front = animal
            self.rear = animal
        else:
            temp = self.rear
            self.rear = animal
            temp.next = animal

    def dequeue(self):
        try:
            self.front.value
        except AttributeError:
            return "this queue is empty!!"
        else:
            temp = self.front
            temp2 = temp.next
            self.front = temp2
            return temp.value


    def __str__(self):
        result = ''
        current = self.front
        while current:
            result += f"{{{current.type}}} -> "
            current = current.next
        return result

if __name__ == '__main__':
    dog = Animal('dog')
    cat = Animal('cat')
    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    print(shelter.__str__())
    shelter.dequeue()
    print(shelter.__str__())