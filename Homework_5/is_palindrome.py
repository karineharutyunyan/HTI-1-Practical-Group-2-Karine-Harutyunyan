def is_palindrome(word):

    for i in range(len(word) // 2):
        if word[0] != word[-1]:
            return 'No'
        else:
            is_palindrome(word[1:-1])
            return 'Yes'


print(is_palindrome(input('Enter a text: ')))
