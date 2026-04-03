# Danh sách sách và giá
books = [
    ("Book 1", 30000),
    ("Book 2", 50000),
    ("Book 3", 100000)
]

total = 0

# Mở file để ghi
with open("book.txt", "w", encoding="utf-8") as f:
    for name, price in books:
        f.write(f"{name};{price}\n")
        total += price

    # Ghi tổng
    f.write(f"Tong;{total}")