def count_vowels(s):
    dem = 0
    for c in s:
        if c.lower() in "aeiou":
            dem = dem + 1
    return dem
s = input()
print(count_vowels(s))