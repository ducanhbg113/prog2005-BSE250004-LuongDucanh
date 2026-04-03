# Nhập số phần tử của mảng
n = int(input("Nhập số phần tử: "))

arr = []

# Nhập các phần tử
for i in range(n):
    x = int(input("Nhập số: "))
    arr.append(x)

# ----- Dòng 1: số lẻ -----
odd_numbers = []

for num in arr:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Các số lẻ:", odd_numbers)
print("Tổng số lượng số lẻ:", len(odd_numbers))


# ----- Hàm kiểm tra số nguyên tố -----
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# ----- Dòng 2: số nguyên tố -----
prime_numbers = []

for num in arr:
    if is_prime(num):
        prime_numbers.append(num)

print("Các số nguyên tố:", prime_numbers)