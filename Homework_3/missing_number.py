def missing_number():
    lst1 = [int(i) for i in number]
    lst2 = [int(j) for j in range(1, len(number) + 2)]
    res = sum(lst2) - sum(lst1)
    print(res)


number = input('Enter numbers separated by space: ').split()
missing_number()
