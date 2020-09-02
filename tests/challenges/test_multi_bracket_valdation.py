from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation():
    expected = multi_bracket_validation('[{]}[({hmm})]')
    assert expected == False

def test_multi_bracket_validation2():
    expected = multi_bracket_validation('{it{should[be]true}here}')
    assert expected == True

def test_multi_bracket_validation3():
    expected = multi_bracket_validation('{}')
    assert expected == True

def test_multi_bracket_validation4():
    expected = multi_bracket_validation('{}(){}')
    assert expected == True

def test_multi_bracket_validation5():
    expected = multi_bracket_validation('()[[Extra Characters]]')
    assert expected == True

def test_multi_bracket_validation6():
    expected = multi_bracket_validation('{}{Code}[Fellows](())')
    assert expected == True

def test_multi_bracket_validation7():
    expected = multi_bracket_validation('[({}]')
    assert expected == False

def test_multi_bracket_validation8():
    expected = multi_bracket_validation('(](')
    assert expected == False

def test_multi_bracket_validation9():
    expected = multi_bracket_validation('{(})')
    assert expected == False