file = "products.txt"
def themsp():
    code = input("Nhập mã sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá: "))

    f = open(file, "a", encoding="utf-8")
    f.write(code + ";" + name + ";" + str(price) + "\n")
    f.close()
    
def hienthi():
    f = open(file, "r", encoding="utf-8")
    for line in f:
        print(line.strip())
    f.close()
def sapxepgia():
    f = open(file, "r", encoding="utf-8")
    ds = []

    for line in f:
        code, name, price = line.strip().split(";")
        ds.append([code, name, float(price)])
        
    f.close()
    ds.sort(key=lambda x: x[2], reverse=True)
    for sp in ds:
        print(sp[0], sp[1], sp[2])
themsp()
print("Danh sách sản phẩm:")
hienthi()
print("Sắp xếp theo giá giảm dần:")
sapxepgia()