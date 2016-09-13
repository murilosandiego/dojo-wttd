import string

def create_list_char():
    chars = string.ascii_letters
    return list(chars)

def create_dict_number_char(list_char):
    dict_char = {}
    for v, k in enumerate(list_char):
        dict_char[k] = v + 1
    return dict_char

def sum_number_char(word, dict_char):
    sum_number = 0
    for k in word:
        sum_number += dict_char[k]
    return sum_number

def calc_number_primo(number):
    palavra_prima = 'Yes'
    
    for n in range(2,number):
        if number % n == 0:
            palavra_prima = 'No'
            break
    return palavra_prima

def calc(word):
    if word == 'a':
        return 'No'

    list_char = create_list_char()
    dict_char_number = create_dict_number_char(list_char) 
    number = sum_number_char(word, dict_char_number)
    palavra_prima = calc_number_primo(number)  

    return palavra_prima


if __name__ == '__main__':
    assert calc('a') == 'No'
    assert calc('d') == 'No'
    assert calc('f') == 'No'

    assert calc('b') == 'Yes'
    assert calc('c') == 'Yes'
    assert calc('e') == 'Yes'

    assert calc('aa') == 'Yes'
    assert calc('ab') == 'Yes'
    assert calc('ad') == 'Yes'

    assert calc('A') == 'No'
    assert calc('Ab') == 'Yes'
    assert calc('ZAc') == 'No'
    assert calc('ZZc') == 'Yes'
    assert calc('ZZe') == 'Yes'
    assert calc('ZZf') == 'No'