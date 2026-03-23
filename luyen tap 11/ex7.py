import csv

ten = input("nhap ten nhan vien: ")
tuoi = input("nhap tuoi: ")
id = input("nhap id: ")

f = open("nhanvien.txt", "w")
f.write("Ten: " + ten + "\n")
f.write("Tuoi: " + tuoi + "\n")
f.write("ID: " + id + "\n")
f.close()

f = open("nhanvien.csv", "w", newline="")
writer = csv.writer(f)
writer.writerow(["Ten", "Tuoi", "ID"])
writer.writerow([ten, tuoi, id])
f.close()

print("da luu file")