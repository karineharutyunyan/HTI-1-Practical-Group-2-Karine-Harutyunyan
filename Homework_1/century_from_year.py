year = int(input('Enter a year between 1 and 2021: '))
if year % 100 == 0:
    print(year // 100)
else:
    print((year // 100) + 1)
