import sys


def utils(start, stop):
    num = range(start, stop)
    for elem in num:
        if start < stop and elem % 2 == 1:
            yield elem


def utils_2(x):
    for elem in x:
        for y in elem:
            if y % 2 == 1:
                yield elem


gen = utils_2(utils(start, stop))

for i in gen:
    print(i)

if __name__ == '__main__':

    if len(sys.argv) = 3:
        start = int(sys.argv[1])
        stop = int(sys.argv[2])
    else:
        print('Please enter 2 integers')
