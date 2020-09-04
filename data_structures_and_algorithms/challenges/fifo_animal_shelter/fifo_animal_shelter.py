# new queue calss it enqueue objects not values..
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, *inp_object):
        for i in inp_object:
            if self.is_empty():
                self.front = i
                self.rear = i
            else:
                self.rear.next = i
                self.rear = i

    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def is_empty(self):
        if self.front == None:
            return True
        return False



class Animal:
    def __init__(self, pet_name):
        self.value = pet_name
        self.next = None

class Cat(Animal):
    type = 'cat'

class Dog(Animal):
    type = 'dog'


class AnimalShelter:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def enqueue(self, *animal):
        '''
        method used to add an animal to the shelter:
            inp ---> animal object only (Cat || Dog)
            out >>> only if the animal not already (Cat || Dog) it return messege..
        '''
        for i in animal:
            if isinstance(i, Cat) or isinstance(i, Dog):
                self.queue1.enqueue(i)
            else:
                return "Animal must be cat or dog"


    def dequeue(self, pref):
        '''
        as queue rules : first enqueue - first dequeue:
            inp ---> it takes type of the animal
            out >>> the animal name..
        '''
        animal = None

        while not self.queue1.is_empty():
            if self.queue1.front.type == pref and animal == None:
                animal= self.queue1.dequeue()
            else:
                self.queue2.enqueue(self.queue1.dequeue())

        while not self.queue2.is_empty():
            self.queue1.enqueue(self.queue2.dequeue())

        return animal.value




if __name__ == '__main__':
    dog = Dog('oscar')
    cat1 = Cat('shery')
    cat2 = Cat('shery2')
    cat3 = Cat('shery3')

    shelter = AnimalShelter()
    shelter.enqueue(dog)
    # shelter.enqueue(cat)

    # print(shelter.dequeue("cat"))
    shelter.enqueue(cat1, cat2, cat3)

    print (shelter.dequeue("cat"))
    print (shelter.dequeue("cat"))



