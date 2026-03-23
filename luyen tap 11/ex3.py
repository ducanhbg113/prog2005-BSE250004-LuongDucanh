ds = []
n = int(input("nhap so luong so: "))
for i in range(n):
    x = int(input("nhap so: "))
    ds.append(x)
tong = 0
for i in ds:
    if i % 2 == 0:
        print(i)
        tong += i
print("tong so chan:", tong)