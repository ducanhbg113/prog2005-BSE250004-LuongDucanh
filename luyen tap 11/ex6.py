d = {}
n = int(input("nhap so nguoi: "))
for i in range(n):
    ten = input("nhap ten: ")
    tuoi = int(input("nhap tuoi: "))
    d[ten] = tuoi
tong = 0
for tuoi in d.values():
    tong += tuoi
print("tuoi trung binh:", tong / len(d))