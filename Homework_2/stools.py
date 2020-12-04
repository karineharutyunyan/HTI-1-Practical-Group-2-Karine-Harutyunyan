def stools():

    height_s = 0
    for i in height_p[:len(height_p)]:
        res = int(max(height_p)) - int(i)
        height_s += int(res)
    print(height_s)


height_p = input('Enter the height: ').split()
stools()
