def diemTB(ds):
    tong = sum(ds.values())
    return tong / len(ds)
students = {
    "lvl": 8,
    "đb": 7,
    "kk": 9}
print("Điểm trung bình:", diemTB(students))