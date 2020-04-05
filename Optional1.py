def is_parsable(x):
    if x.isdigit():
        return True
    else:
        return False


def pyramid_with_given_height(input):
    if is_parsable(input) and int(input) > 0:
        rows = int(input)
        for i in range(rows):
            print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    else:
        print("Please enter a integer greater than 0")


rows = input("Please enter the height of our pyramid : ")
pyramid_with_given_height(rows)