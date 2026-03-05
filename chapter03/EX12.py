m = int(input())
n = int(input())
a = []
b = []
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)
c = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(a[i][j] + b[i][j])
    c.append(row)
for i in range(m):
    print(c[i])