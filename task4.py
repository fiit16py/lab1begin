def is_power_of_two(n):
        i=2
        while i<1000000:
                if i==n:
                        print('true')
                        break
                i*=2
        else: print('false')
pass

n = int(input())
print(is_power_of_two(n))
