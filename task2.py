def digit_sum(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n = n // 10
    return (sum)

print('Введите число')
n = int(input())
print(digit_sum(n))
