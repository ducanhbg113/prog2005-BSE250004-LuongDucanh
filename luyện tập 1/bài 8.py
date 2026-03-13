class Student:
    def __init__(self, ten, diem):
        if diem < 0 or diem > 10:
            print("Điểm quá ảo")
        else:
            self.ten = ten
            self.diem = diem
sv1 = Student("lvl", 8)
sv2 = Student("đb", 11)
print("Sinh viên 1:", sv1.ten, "-", sv1.diem)