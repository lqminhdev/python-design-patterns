class Circle:
    @staticmethod
    def draw():
        print('draw a circle')


class Square:
    @staticmethod
    def draw():
        print('draw a square')


class Red:
    @staticmethod
    def fill():
        print('fill red')


class Blue:
    @staticmethod
    def fill():
        print('fill blue')


class AbstractFactory:
    def get_shape(self, s):
        pass

    def get_color(self, c):
        pass


class ShapeFactory(AbstractFactory):
    def get_shape(self, s):
        if s == 'C':
            return Circle()
        elif s == 'S':
            return Square()


class ColorFactory(AbstractFactory):
    def get_color(self, c):
        if c == 'R':
            return Red()
        elif c == 'B':
            return Blue()


class ProduceFactory:
    @staticmethod
    def get_factory(f):
        if f == 'shape':
            return ShapeFactory()
        elif f == 'color':
            return ColorFactory()


if __name__ == '__main__':
    shape_factory = ProduceFactory().get_factory('shape')
    circle = shape_factory.get_shape('C')
    circle.draw()

    color_factory = ProduceFactory().get_factory('color')
    red = color_factory.get_color('R')
    red.fill()