chuoi = []

for i in range(5):
    s = input("nhap chuoi: ")
    chuoi.append(s)

for i in range(1, len(chuoi)):
    key = chuoi[i]
    j = i - 1

    while j >= 0 and len(chuoi[j]) < len(key):
        chuoi[j + 1] = chuoi[j]
        j = j - 1
        print(chuoi)

    chuoi[j + 1] = key
    print(chuoi)