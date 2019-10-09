def get_largest_perimiter(L):
    n = len(L)
    if n < 3:
        return 0
    mx = 0
    for x in range(n - 2):
        for y in range(x + 1, n - 1):
            for z in range(y + 2, n):
                a = L[x]
                b = L[y]
                c = L[z]
                if a + b < c or a + c < b or c + b < a:
                    continue
                mx = max(mx, a + b + c)
    return mx

L = [int(i) for i in input().split()]
print(get_largest_perimiter(L))
