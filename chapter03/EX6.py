a = list(map(int, input().split()))
swap = 0
for x in range(len(a)):
    for y in range(0, len(a) - x - 1):
        if a[y] > a[y + 1]:
            t = a[y]
            a[y] = a[y + 1]
            a[y + 1] = t
            swap = swap + 1
print(a)
print(swap)