def roman_to_integer(letter):

    letter = list(letter)
    s = 0

    for i in range(0, len(letter)):
        n = i - 1
        m = i + 1

        if n < 0:
            n += 1

        if m >= len(letter):
            m -= 1

        if letter[i] == "I" and letter[m] != "V" and letter[m] != "X":
            s += 1
        elif letter[i] == "I" and letter[m] == "X":
            s += 9
        elif letter[i] == "I" and letter[m] == "V":
            s += 4
        elif letter[i] == "V" and letter[n] != "I":
            s += 5
        elif letter[i] == "X" and letter[n] != "I" and letter[m] != "L" and letter[m] != "C":
            s += 10
        elif letter[i] == "X" and letter[m] == "L":
            s += 40
        elif letter[i] == "L" and letter[n] != "X":
            s += 50
        elif letter[i] == "X" and letter[m] == "C":
            s += 90
        elif letter[i] == "C" and letter[n] != "X" and letter[m] != "M" and letter[m] != "D":
            s += 100
        elif letter[i] == "C" and letter[m] == "D":
            s += 400
        elif letter[i] == "D" and letter[n] != "C":
            s += 500
        elif letter[i] == "C" and letter[m] == "M":
            s += 900
        elif letter[i] == "M" and letter[n] != "C":
            s += 1000

    return s


roman = input("Enter Roman numerals: ")
print(roman_to_integer(roman))
