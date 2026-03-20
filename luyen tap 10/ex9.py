class Nguoi:
    def __init__(self, ten, tuoi):
        self.set_ten(ten)
        self.set_tuoi(tuoi)

    def get_ten(self):
        return self._ten

    def set_ten(self, ten):
        if not ten:
            raise ValueError("Ten khong duoc rong")
        self._ten = ten

    def get_tuoi(self):
        return self._tuoi

    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuoi phai lon hon hoac bang 0")
        self._tuoi = tuoi

    def __str__(self):
        return f"{self._ten}, {self._tuoi} tuoi"

    def gioi_thieu(self):
        return f"Xin chao, toi la {self._ten}"

    @classmethod
    def tu_lop(cls):
        return cls("Nguyen Van A", 30)

    @staticmethod
    def thong_bao():
        return "Day la static method"

    def __eq__(self, other):
        return self._ten == other._ten and self._tuoi == other._tuoi


class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, lop):
        super().__init__(ten, tuoi)
        self.set_lop(lop)

    def get_lop(self):
        return self._lop

    def set_lop(self, lop):
        if not lop:
            raise ValueError("Lop khong duoc rong")
        self._lop = lop

    def __str__(self):
        return f"{self._ten}, {self._tuoi} tuoi, lop {self._lop}"

    def thong_tin_sinh_vien(self):
        return f"Sinh vien: {self._ten}, lop {self._lop}"


# VD su dung
n = Nguoi("An", 25)
print(n)
print(n.gioi_thieu())
print(Nguoi.thong_bao())
m = Nguoi.tu_lop()
print(m)

sv = SinhVien("Binh", 20, "12A1")
print(sv)
print(sv.thong_tin_sinh_vien())