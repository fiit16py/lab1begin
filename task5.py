def is_prime(n):
        if n > 1:
                val = 2
                while val <= n / 2:
                        if n % val == 0:
                                return 'false'
                        else:
                                val+=1
                return 'true'
        else:
                return 'false'
n = int(input())
print(is_prime(n))
