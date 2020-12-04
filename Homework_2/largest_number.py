def largest_number():

    sum_1 = 0
    for i in num[0:len(num):2]:
        sum_1 += int(i)

    sum_2 = 0
    for i in num[1:len(num):2]:
        sum_2 += int(i)

    if sum_1 == sum_2:
        print('Yes')
    else:
        print('No')


num = input('Enter a number: ')
largest_number()

