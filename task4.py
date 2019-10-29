def is_power_of_two(n):
        while(n>1):
                if(n%2==0):
                        n=n/2
                else:
                        return False
        return True

n = int(input())
print(is_power_of_two(n))
