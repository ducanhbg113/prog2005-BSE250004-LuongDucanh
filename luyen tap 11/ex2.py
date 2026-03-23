chuoilist = []

for i in range(5):
    s = input("nhap chuoi: ")
    chuoilist.append(s)

chuoilist.sort()

print("danh sach sau khi sap xep:", chuoilist)

x = input("nhap chuoi can tim: ")

left = 0
right = len(chuoilist) - 1
timthay = False

while left <= right:
    mid = (left + right) // 2

    if chuoilist[mid] == x:
        print("tim thay o vi tri:", mid)
        timthay = True
        break
    elif chuoilist[mid] < x:
        left = mid + 1
    else:
        right = mid - 1

if not timthay:
    print("khong tim thay")