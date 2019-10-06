def is_power_of_two(n):
        l = []
        for i in range(30):
                l.append(2 ** i)
        if n in l:
                return True
        else:
                return False

n = 1

while(n != 0):
        n = int(input())
        print(is_power_of_two(n))
