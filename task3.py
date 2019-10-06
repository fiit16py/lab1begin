def is_beautiful(n):
        a = 0
        z = n
        while(n > 0):
                a = a + n % 10
                n = n // 10
        if z % a == 0:
                return True
        else:
                return False
n = 1

while(n != 999):
        n = int(input())
        print(is_beautiful(n))
