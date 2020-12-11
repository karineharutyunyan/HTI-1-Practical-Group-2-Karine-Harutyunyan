def segment_length(x1, y1, x2, y2):

    len_1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return len_1


def segment_length_2(x2, y2, x3, y3):

    len_2 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    return len_2


def rectangle_perimeter(length_1, length_2):

    rec_per = (length_1 + length_2) * 2
    print(rec_per)


number = input('Enter coordinates of a rectangle(x1, y1, x2, y2, x3, y3, x4, y4): ').split()
x1, y1, x2, y2, x3, y3, x4, y4 = (float(i) for i in number)
length_1 = segment_length(x1, y1, x2, y2)
length_2 = segment_length_2(x2, y2, x3, y3)
rectangle_perimeter(length_1, length_2)
