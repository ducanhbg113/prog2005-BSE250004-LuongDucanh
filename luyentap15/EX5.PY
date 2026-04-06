def count_vowels(s):
    dem = 0
    for c in s.lower():
        if c in "aeiou":
            dem += 1
    return dem
s = input("nhap chuoi: ")
print(count_vowels(s))