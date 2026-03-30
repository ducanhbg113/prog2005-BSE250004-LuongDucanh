class Flower:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


f = Flower("Red")

print(f.get_color())

f.set_color("Blue")

print(f.get_color())