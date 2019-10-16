def get_largest_perimiter(L):
    largest_per = -1
    for i in range(len(L) - 2):
        for j in range(i, len(L) - 1):
            for k in range(j, len(L)):
                a = L[i]
                b = L[j]
                c = L[k]
                if  a + b > c and a + c > b and b + c > a and a + b + c > largest_per:
                    largest_per = a + b + c
    return largest_per
L = list(map(int, input().split()))
print(get_largest_perimiter(L))
