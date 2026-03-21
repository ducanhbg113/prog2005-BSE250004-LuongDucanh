import matplotlib.pyplot as plt
sp = ["A", "B", "C", "D", "E"]
pt = [30, 25, 15, 20, 10]
plt.pie(pt, labels=sp, autopct="%1.1f%%")
plt.title("Phan tram doanh so cac san pham")
plt.show()