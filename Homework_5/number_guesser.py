def number_guesser(guess_num, lower, upper):

    chance = 0
    number = ((upper - lower) // 2 + lower)

    while chance != 10:
        chance += 1
        print('My guess number:', number)

        guess_num = input()
        if guess_num == '0':
            return 'I guessed in 10 steps!'

        elif guess_num == '1':
            return number_guesser(guess_num, number, upper)

        elif guess_num == '-1':
            return number_guesser(guess_num, lower, number)

        else:
            return 'I could not guess in 10 steps! This means you cheated!'


number_guesser(input('Think of a number between 1 and 999. Input 0 once you’re ready to play: '), 0, 1000)
