from data_structures_and_algorithms.challenges.hashtable.hashtable import Hash_table

test = Hash_table(5)

def test_create_empty_hash_table():
    assert test.__str__() == 'hash table is empty!!'

def test_hashing():
    assert test.hash('cat') == 4
    
def test_hashing_in_range_HT_size():
    assert test.hash('cat') <= 5
    assert test.hash('whatever..') <= 5

def test_add():
    test.add('cat', 'hi')
    assert test.__str__() == "in index: 4 : ('cat', 'hi') \n"

def test_add_duplicate():
    test.add('cat', 'hello_TAs')
    test.add('cat', 'glad to see you guys.. :)')
    assert test.__str__() == "in index: 4 : ('cat', 'glad to see you guys.. :)') \n"

def test_add_in_hashed_key_as_index():
    test.add('cat', 'hello_TAs')
    hashed_key = test.hash('cat')
    assert test.__str__() == f"in index: {hashed_key} : ('cat', 'hello_TAs') \n"

def test_handle_collision():
    test.add('cat', 'hello_TAs')
    test.add('tac', 'glad to see you guys.. :)')
    hashed_key = test.hash('cat')
    assert test.__str__() == f"in index: {hashed_key} : ('cat', 'hello_TAs') >> ('tac', 'glad to see you guys.. :)') \n"

def test_get_with_no_collision():
    test.add('cat', 'hello_TAs')
    test.add('fatCat', 'how you doin...')
    assert test.get('fatCat') == 'how you doin...'

def test_get_with_collision():
    test.add('cat', 'hello_TAs')
    test.add('tac', 'glad to see you guys.. :)')
    test.add('cta', 'how you doin...')
    test.add('atc', "joy doesn't share food!")
    assert test.get('tac') == 'glad to see you guys.. :)'

def test_get_not_exists():
    test.add('cat', 'hello_TAs')
    test.add('tac', 'glad to see you guys.. :)')
    test.add('cta', 'how you doin...')
    test.add('atc', "joy doesn't share food!")
    assert test.get('notKey') == 'null'

def test_contains_true():
    test.add('cat', 'hello_TAs')
    test.add('tac', 'glad to see you guys.. :)')
    test.add('cta', 'how you doin...')
    test.add('atc', "joy doesn't share food!")
    assert test.contains('cta') == True

def test_contains_false():
    test.add('cat', 'hello_TAs')
    test.add('tac', 'glad to see you guys.. :)')
    test.add('cta', 'how you doin...')
    test.add('atc', "joy doesn't share food!")
    assert test.contains('notEvenACat!') == False
