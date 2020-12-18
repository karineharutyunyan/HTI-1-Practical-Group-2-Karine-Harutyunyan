def roman_to_integer_2(letter):
    my_dict = {'IV': '4', 'IX': '9', 'XL': '40', 'XC': '90', 'CD': '400', 'CM': '900', 'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}

    arabic = 0
    for i in range(len(letter)):
        if my_dict[letter[i]] >= my_dict[letter[i - 1]]:
            arabic += my_dict[letter[i]] - 2 * my_dict[letter[i - 1]]
        else:
            arabic += my_dict[letter[i]]

    return arabic


roman = input("Enter Roman numerals: ")
print(roman_to_integer_2(roman))
