print ("nhập số từ 1 đến 9")
n = int(input())
if n >9 or n <1:
    print("sai điều kiện")
else:
  for i in range (1,11):
    print(n,"x",i,"=", n * i)
    