names = []

# Nhập 5 tên từ bàn phím
for i in range(5):
    name = input("Nhập tên: ")
    names.append(name)

print("Danh sách sau khi nhập:", names)

# Xóa người ở vị trí thứ hai (index = 1)
del names[1]

print("Danh sách sau khi xóa:", names)