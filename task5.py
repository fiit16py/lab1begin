def is_prime(n):
        d = 2
        while d * d <= n and n % d != 0:
                d += 1
        return d * d > n
pass

n = int(input())
print(is_prime(n))
