def toan(t):
    tong = sum(t)
    lonnhat = max(t)
    nhonhat = min(t)
    return tong, lonnhat, nhonhat
ss = (3, 7, 2, 9, 5)
kq = toan(ss)
print("Tổng:", kq[0])
print("Lớn nhất:", kq[1])
print("Nhỏ nhất:", kq[2])