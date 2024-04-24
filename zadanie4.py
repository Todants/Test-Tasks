def multiplication_table(num):
    max_width = len(str(num * num))

    print("{:>{}}".format(' ', max_width), end="  ")
    for i in range(1, num + 1):
        print("{:>{}}".format(i, max_width), end="  ")
    print()
    
    for i in range(1, num + 1):
        print("{:>{}}".format(i, max_width), end="  ")
        for j in range(1, num + 1):
            print("{:>{}}".format(i * j, max_width), end="  ")
        print()

if __name__ == "__main__":
    multiplication_table(12)
