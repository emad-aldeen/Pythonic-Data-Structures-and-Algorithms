from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import *

def test_fifo_animal_shelter1():
    dog = Dog('oscar')
    cat1 = Cat('shery')
    cat2 = Cat('shery2')
    cat3 = Cat('shery3')

    shelter = AnimalShelter()
    shelter.enqueue(dog)
    shelter.enqueue(cat1, cat2, cat3)

    assert shelter.dequeue("cat") == 'shery'

def test_fifo_animal_shelter2():
    dog1 = Dog('oscar')
    dog2 = Dog('oscar2')
    dog3 = Dog('oscar3')

    cat1 = Cat('shery')
    cat2 = Cat('shery2')
    cat3 = Cat('shery3')

    shelter = AnimalShelter()
    shelter.enqueue(dog1, dog2, dog3)
    shelter.enqueue(cat1, cat2, cat3)

    assert shelter.dequeue("dog") == 'oscar'

def test_fifo_animal_shelter3():
    dog1 = Dog('oscar')
    dog2 = Dog('oscar2')
    dog3 = Dog('oscar3')

    cat1 = Cat('shery')
    cat2 = Cat('shery2')
    cat3 = Cat('shery3')

    shelter = AnimalShelter()
    shelter.enqueue(dog1, dog2, dog3)
    shelter.enqueue(cat1, cat2, cat3)

    shelter.dequeue("dog")
    assert shelter.dequeue("dog") == 'oscar2'

def test_fifo_animal_shelter4():
    dog1 = Dog('oscar')
    dog2 = Dog('oscar2')
    dog3 = Dog('oscar3')

    cat1 = Cat('shery')
    cat2 = Cat('shery2')
    cat3 = Cat('shery3')

    shelter = AnimalShelter()
    shelter.enqueue(dog1, dog2, dog3)
    shelter.enqueue(cat1, cat2, cat3)

    shelter.dequeue("dog")
    shelter.dequeue("dog")
    assert shelter.dequeue("dog") == 'oscar3'


def test_fifo_animal_shelter5():
    not_dog = AnimalShelter()

    shelter = AnimalShelter()
    assert shelter.enqueue(not_dog) == 'Animal must be cat or dog'


