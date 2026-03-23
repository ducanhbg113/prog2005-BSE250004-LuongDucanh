r = int(input("nhap so hang: "))
c = int(input("nhap so cot: "))

A = []
B = []

print("nhap ma tran A")
for i in range(r):
    row = []
    for j in range(c):
        x = input("nhap gia tri: ")
        if x == "":
            print("loi: gia tri rong")
            exit()
        row.append(int(x))
    A.append(row)

print("nhap ma tran B")
for i in range(r):
    row = []
    for j in range(c):
        x = input("nhap gia tri: ")
        if x == "":
            print("loi: gia tri rong")
            exit()
        row.append(int(x))
    B.append(row)

C = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("ma tran tong:")
for i in C:
    print(i)