a = list(map(int, input().split()))
kq = -1
for x in a:
    if x > 10:
        kq = x
        break
print(kq)