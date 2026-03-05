a = list(map(int, input().split()))
x = int(input())
kq = -1
for i in range(len(a)):
    if a[i] == x:
        kq = i
        break
print(kq)