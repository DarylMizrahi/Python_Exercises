import math

my_list=[x**2 for x in range(1,10) if x %2!=0]

my_list2 = [math.sqrt(x) for x in range(1,10) if x % 2 ==0]

print(my_list)
print(my_list2)