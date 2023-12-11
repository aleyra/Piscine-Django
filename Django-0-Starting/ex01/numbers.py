def read_print():
    f = open('numbers.txt', 'r')
    lst = f.readline().split(',')
    for l in lst:
        print(l)


if __name__ == "__main__":
    read_print()
