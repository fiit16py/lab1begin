def get_largest_perimiter(L):
    l = list(L)
    s = 0
    for a in range(len(l) - 2):
        for b in range(a + 1, len(l) - 1):
            for c in range(b + 1, len(l)):
                if l[a] + l[b] > l[c] and l[a] + l[c] > l[b] and l[b] + l[c] > l[a]:
                    if s < (l[a] + l[b] + l[c]):
                        s = l[a] + l[b] + l[c]
    return s


L = map(int, input().split())
print(get_largest_perimiter(L))
