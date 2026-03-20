chuoi = input("nhap chuoi: ")
ky_tu = input("nhap ky tu: ")
dem = 0
for c in chuoi:
    if c == ky_tu:
        dem += 1
print("so lan xuat hien:", dem)