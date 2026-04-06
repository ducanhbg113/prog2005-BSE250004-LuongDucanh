def luu_chuoi():
    s = input("nhap chuoi: ")
    f = open("data.txt", "w")
    f.write(s)
    f.close()

luu_chuoi()