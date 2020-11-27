num = input('Enter a number: ')

result = 1

for digit in num:
    if digit != '0':
        result = result * int(digit)

print(result)