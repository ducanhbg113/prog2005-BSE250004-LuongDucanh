i = 1
tong = 0

while i <= 30:
    if i % 2 != 0:
        print(i)
        tong += i
    i += 1

print("Tổng các số lẻ:", tong)