sv = {"Ab": 8,"cc": 7,"kk": 9}
def tinh_tb(d):
    tong = 0
    for diem in d.values():
        tong += diem
    return tong / len(d)

print(tinh_tb(sv))