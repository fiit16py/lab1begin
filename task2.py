def digit_sum(n):
    s=0
    while n>0:
        a=n%10
        s=s+a
        n//=10
    print(s)
    pass

print('Введите число')
n = int(input())
print(digit_sum(n))
