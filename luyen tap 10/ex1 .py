def music(path):
    return path.split("\\")[-1]
def nhacbolero(path):
    ten_file = path.split("\\")[-1]
    return ten_file.split(".")[0]
path = "d:\\music\\muabui.mp3"
print(mucsic(path))
print(nhacbolero(path))