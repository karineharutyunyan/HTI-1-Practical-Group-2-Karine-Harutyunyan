input_string = input('Enter numbers separated by space: ')
lst1 = [int(num) for num in input_string.split()]
lst2 = lst1.copy()
del lst2[0]
res = list(map(lambda x, y: x*y, lst1, lst2))
print(max(res))
