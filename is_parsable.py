def is_parsable(x):
    if x.isdigit():
        print("nice")
        return True
    else:
        print("false")
        return False



is_parsable(input("User input: "))