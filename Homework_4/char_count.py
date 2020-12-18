def char_count(s):

    my_dict = {char: s.count(char) for char in s}
    return my_dict


symbol = input('Enter: ')
print(char_count(symbol))
