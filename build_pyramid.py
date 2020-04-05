
def build_pyramid(rows):
    for i in range(rows):
        print(" "*(rows - i - 1) + "*"*(2 * i + 1))


rows = int(input("Choose the pyramid's height: "))
build_pyramid(rows)

