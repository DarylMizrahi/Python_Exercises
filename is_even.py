def is_even(x):
    if x.isdigit():
        if int(x) % 2 == 0:
            return True
        else:
            print("False")
            return False
    else:
        print("This wasn't an integer. Thanks for trying, goodbye.")
        exit()



is_even(input("please give me a number "))