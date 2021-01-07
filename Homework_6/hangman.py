import random


def get_a_word():
    with open('fruits.txt') as f:
        word = random.choice(f.readlines())
        return word.upper()


def hangman(word):
    guessed = False
    length = '_' * (len(word) - 1)
    secret_word = list(word)
    mistakes = 5

    while not guessed and mistakes > 0:
        print(f'Guess the word. {mistakes} mistakes left.')
        print(length)
        guess = input('Guess a letter: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in secret_word:
                index = secret_word.index(guess)
                length_list = list(length)
                length_list[index] = guess
                index += 1
                length = ''.join(length_list)
                if '_' not in length:
                    guessed = True
            elif guess not in word:
                mistakes -= 1

        elif len(guess) == (len(word) - 1) and guess.isalpha():
            if guess in word:
                print(word)
                print('You won the game')
            elif guess != word:
                print(guess, 'is not the word.')
                mistakes -= 1

        else:
            print('Not a valid guess.')
            mistakes -= 1

    if guessed:
        print(word)
        print('You won the game')
    else:
        print('You lost the game.')


def main():
    word = get_a_word()
    hangman(word)


if __name__ == "__main__":
    main()
