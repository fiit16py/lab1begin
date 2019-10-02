def is_beautiful(n):
        sum = 0
        m = n
        while (n > 0):
                sum += n % 10
                n = n // 10
        if (m % sum == 0):
                return('true')
        else:
                return('false')

n = int(input())
print(is_beautiful(n))
