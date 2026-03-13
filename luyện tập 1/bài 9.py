class Student:
    def __init__(self, ten, diem):
        if diem < 0 or diem > 10:
            print("Điểm quá ảo")
        else:
            self.ten = ten
            self.diem = diem
    def display(self):
        print("Sinh viên", self.ten, "có điểm", self.diem)
sv1 = Student("lvl", 10)
sv2 = Student("đb", 8)
sv1.display()
sv2.display()