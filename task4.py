def is_power_of_two(n):
    if n & (n - 1):
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
        n = int(input())
        print(is_power_of_two(n))
