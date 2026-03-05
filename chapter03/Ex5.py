abc = list(map(float, input().split()))
for A in range(1, len(abc)):
    key = abc[A]
    A = A - 1
    while A >= 0 and abc[A] < key:
        abc[A + 1] = abc[A]
        A = A- 1
    abc[A + 1] = key
print(abc)