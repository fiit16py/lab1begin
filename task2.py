def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


print('Введите число')
n = int(input())
print(digit_sum(n))
