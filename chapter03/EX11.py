a = list(map(int, input().split()))
max = a[0]
min = a[0]
for x in a:
    if x > max:
        max = x
    if x < min:
        min = x
print(max)
print(min)