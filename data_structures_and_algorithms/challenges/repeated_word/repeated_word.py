from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList

def repeated_word(string):
    '''
    using linked list this function will search for the first repeated word in your inputed string:
        inp ---> only string
        out >>> the repeated word from your input
    '''
    container = LinkedList()
    word = ''
    for i in range(len(string)):
        if container.includes(word):
            # print(container.toString())
            return word
        elif string[i] == ',' or string[i] == ' ' or string[i] == '-' or string[i] == '.' :
            if word != '': 
                container.insert(word)
                word = ''
            continue
        else:
            word += string[i].lower()
    # print(container.toString())
    return 'there is no repeated word in your input!'



if __name__ == '__main__':
    expected = repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...")
    assert expected == 'summer'
    print('test passed!!')
