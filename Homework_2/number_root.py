def number_root():

    sum_1 = 0
    for i in numbers[:len(numbers)]:
        sum_1 += int(i)

    if sum_1 < 9:
        print(sum_1)
    else:
        sum_2 = 0
        sum_1 = str(sum_1)
        for j in sum_1[:len(sum_1)]:
            sum_2 += int(j)
        print(sum_2)


numbers = input('Enter a number:')
number_root()

