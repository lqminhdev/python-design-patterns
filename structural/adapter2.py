class Color:
    @staticmethod
    def draw_color():
        return 'Red'

    @staticmethod
    def make_color():
        return 'Blue'


class ColorAdapter:
    def __init__(self, Color):
        self.obj = Color

    def get_color(self):
        return self.obj.draw_color()
        # return self.obj.make_color()


if __name__ == '__main__':
    c = ColorAdapter(Color)
    print(c.get_color())