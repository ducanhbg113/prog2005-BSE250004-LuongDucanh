import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("california_cities.csv")
top10 = df.sort_values("area_total_km2", ascending=False).head(10)
plt.barh(top10["city"], top10["area_total_km2"])
plt.title("Top 10 thanh pho lon nhat o California theo dien tich")
plt.xlabel("Dien tich (km2)")
plt.ylabel("Thanh pho")
plt.gca().invert_yaxis()
plt.show()