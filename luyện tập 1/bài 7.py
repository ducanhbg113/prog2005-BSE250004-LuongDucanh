class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
sv1 = Student("lol", 8)
sv2 = Student("đb", 9)
print("Sinh viên 1:", sv1.ten, "-", sv1.diem)
print("Sinh viên 2:", sv2.ten, "-", sv2.diem)