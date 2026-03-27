#bài 1
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
print("tổng:", a + b )
print("hiệu:", a - b )
print("tích:",a*b)
print("thương:", a/b) 
print("kkk")

# bài 2
tên = input("nhập tên vào:")
năm_sinh = int (input("năm sinh :"))
tuổi = 2026 - năm_sinh
print("tên:", tên)
print("tuổi:", tuổi)

# bài 3
n = int(input("nhập n:"))
for i in range(1,n+1):
    if i % 2 ==0:
        print(i)
        
#bài 4
n = int(input("nhập n:"))
tong= 0
for i in range (1,n+1):
    if i % 3 == 0:
     tong += i
    print("tổng=", tong)
    
#bài 5 
n = int(input("Nhập số lượng phần tử: "))
numbers = []
for i in range(n):
    x = int(input("Nhập số: "))
    numbers.append(x)
print("Số lớn nhất:", max(numbers))

#bài 6
s = input("Nhập các số cách nhau bằng dấu cách: ")

numbers = list(map(int, s.split()))

count = 0

for num in numbers:
    if num < 0:
        count += 1

print("Số nguyên âm:", count)

#bài 7
class SinhVien:
    def __init__(self, ten, tuoi, lop):
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop

    def hien_thi(self):
        print("Tên:", self.ten)
        print("Tuổi:", self.tuoi)
        print("Lớp:", self.lop)


ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))
lop = input("Nhập lớp: ")

sv = SinhVien(ten, tuoi, lop)
sv.hien_thi()

#bài8
class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def dien_tich(self):
        return self.dai * self.rong

    def chu_vi(self):
        return (self.dai + self.rong) * 2


d = float(input("Nhập chiều dài: "))
r = float(input("Nhập chiều rộng: "))

hcn = HinhChuNhat(d, r)

print("Diện tích:", hcn.dien_tich())
print("Chu vi:", hcn.chu_vi())

#bài9
numbers = input("Nhập các số cách nhau bằng dấu cách: ")

with open("đb.txt", "w") as f:
    f.write(numbers)

print("Đã ghi vào file đb.txt")

#bài 10
import matplotlib.pyplot as plt

with open("concak.txt", "r") as f:
    data = f.read()

numbers = list(map(int, data.split()))

plt.bar(range(len(numbers)), numbers)
plt.title("Biểu đồ cột")
plt.show()