def is_uppercase():
    for letter in word:
        if letter.isupper():
            print('Yes')
        else:
            print('No')


word = input('Enter a word: ').split()
is_uppercase()

