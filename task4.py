def is_power_of_two(n):
        if math.log(n, 2).is_integer():
                return 'true'
        else:
                return 'false'


import math
n = int(input())
print(is_power_of_two(n))
