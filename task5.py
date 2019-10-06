def is_prime(n):
        a = 2
        while(n % a != 0):
                a += 1
        if a == n:
                return True
        else:
                return False

n = 1

while(n != 0):
        n = int(input())
        print(is_prime(n))
