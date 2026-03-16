class SinhVien:
    count = 0
    def __init__(self, ten):
        self.ten = ten
        SinhVien.count += 1
    @classmethod
    def dem(cls):
        return cls.count
sv1 = SinhVien("trump")
sv2 = SinhVien("obama")
sv3 = SinhVien("binladen")
print("Số đối tượng SinhVien:", SinhVien.dem())