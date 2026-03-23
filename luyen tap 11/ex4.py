 ds = [1, 3, 5, 7, 2]
x = int(input("nhap so can them: "))
ds.append(x)
k = int(input("nhap k: "))
dem = ds.count(k)
print("so lan xuat hien:", dem)
tong = 0
for n in ds:
    if n > 1:
        la_snt = True
        for i in range(2, n):
            if n % i == 0:
                la_snt = False
                break
        if la_snt:
            tong += n

print("tong so nguyen to:", tong)
ds.sort()
print("danh sach sau khi sap xep:", ds)
ds.clear()
print("danh sach sau khi xoa:", ds)