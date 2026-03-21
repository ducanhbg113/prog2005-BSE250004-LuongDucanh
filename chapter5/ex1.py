import matplotlib.pyplot as plt
loai = ["Xuat sac", "Gioi", "Trung binh", "Yeu", "ngu"]
soluong = [6, 10, 12, 4, 1]
plt.bar(loai, soluong)
plt.title("Ket qua hoc tap cua lop")
plt.xlabel("Loai hoc luc")
plt.ylabel("So luong hoc sinh")
plt.show()