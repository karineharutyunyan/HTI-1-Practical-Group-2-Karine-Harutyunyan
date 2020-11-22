a = int(input('First side: '))
b = int(input('Second side: '))
c = int(input('Third side: '))

sides = [a, b, c]
sides.sort()
a = sides[0]
b = sides[1]
c = sides[2]

if c >= a + b:
    print('Not a triangle')
elif c * c == a * a + b * b:
    print('Right triangle')
elif c * c > a * a + b * b:
    print('Obtuse triangle')
elif c * c < a * a + b * b:
    print('Acute triangle')
else:
    print('Not a triangle')
