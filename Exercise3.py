import math

def list_square_even_power_odd():
    power_odd = [x**2 for x in range(1, 10) if x % 2 != 0]
    square_even = [math.sqrt(x) for x in range(1, 10) if x % 2 == 0]
    print(str(power_odd))
    print(str(square_even))


list_square_even_power_odd()