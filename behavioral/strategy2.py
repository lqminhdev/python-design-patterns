
class Color:
    def __init__(self, func=None):
        self.name = 'Default color'
        if func:
            func(self)

    def execute(self):
        print(self.name)


def red_color(self):
    self.name = 'Red'


def blue_color(self):
    self.name = 'Blue'


if __name__ == '__main__':
    c = Color()
    c1 = Color(red_color)
    c2 = Color(blue_color)

    c.execute()
    c1.execute()
    c2.execute()


