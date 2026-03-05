s = input()
print(s[::-1])
rev = ""
for c in s:
    rev = c + rev
print(rev)