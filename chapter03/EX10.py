a = list(map(int, input().split()))
tong = 0
for chan in a:
    if chan % 2 == 0:
        print(chan)
        tong = tong + chan
print(tong)