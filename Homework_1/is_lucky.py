num = input('Enter numbers between 10 and 999999 ')

num = str(num)

start = num[0:(len(num) // 2)]
end = num[(len(num) // 2):len(num)]
if sum(start) == sum(end):
    print('Yes')
if sum(start) != sum(end):
    print('No')
