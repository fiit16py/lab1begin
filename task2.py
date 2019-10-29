def digit_sum(n):
    s=0
    while (n//10>0):
        s=s+n%10
        n=n//10
    s=s+n
    return s

print('Введите число')
n = int(input())
print(digit_sum(n))
