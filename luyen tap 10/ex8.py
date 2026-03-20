chuoi_list = []

for i in range(5):
    chuoi = input(f"nhap chuoi {i+1}: ")
    chuoi_list.append(chuoi)

n = len(chuoi_list)

for i in range(n):
    for j in range(0, n-i-1):
        if len(chuoi_list[j]) < len(chuoi_list[j+1]):
            chuoi_list[j], chuoi_list[j+1] = chuoi_list[j+1], chuoi_list[j]
        print(chuoi_list)