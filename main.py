from abc import ABC, abstractmethod

END = '\033[0'
START = '\033[1;38;2'
MOD = 'm'


class ComputerColor(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __rmul__(self, other):
        pass


class Color(ComputerColor):
    def __init__(self, r: int, g: int, b: int):
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError('incorrect color')

        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return f'{START};{self.r};{self.g};{self.b}{MOD}●{END}{MOD}'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Color):
            red = min(self.r + other.r, 255)
            green = min(self.g + other.g, 255)
            blue = min(self.b + other.b, 255)
            return Color(red, green, blue)
        return NotImplemented

    def _contrasted_colors(self, c: float) -> tuple:
        if c < 0:
            c = 0
        elif c > 1:
            c = 1
        cl = -256 * (1 - c)
        F = (259 * (cl + 255)) / (255 * (259 - cl))
        r = int(F * (self.r - 128) + 128)
        g = int(F * (self.g - 128) + 128)
        b = int(F * (self.b - 128) + 128)
        return r, g, b

    def __rmul__(self, other):
        if isinstance(other, float):
            r, g, b = self._contrasted_colors(other)
            return Color(r, g, b)
        return NotImplemented

    def __mul__(self, other):
        return self.__rmul__(other)

    def __hash__(self):
        return hash((self.r, self.g, self.b))


def print_a(color: ComputerColor):
    bg_color = 0.2 * color
    a_matrix = [
        [bg_color] * 19,
        [bg_color] * 9 + [color] + [bg_color] * 9,
        [bg_color] * 8 + [color] * 3 + [bg_color] * 8,
        [bg_color] * 7 + [color] * 2 + [bg_color] + [color] * 2 + [bg_color] * 7,
        [bg_color] * 6 + [color] * 2 + [bg_color] * 3 + [color] * 2 + [bg_color] * 6,
        [bg_color] * 5 + [color] * 9 + [bg_color] * 5,
        [bg_color] * 4 + [color] * 2 + [bg_color] * 7 + [color] * 2 + [bg_color] * 4,
        [bg_color] * 3 + [color] * 2 + [bg_color] * 9 + [color] * 2 + [bg_color] * 3,
        [bg_color] * 19,
    ]

    for row in a_matrix:
        print(''.join(str(ptr) for ptr in row))


if __name__ == '__main__':
    print(Color(128, 0, 0) * 0.5)

    red = Color(255, 0, 0)
    blue = Color(0, 0, 255)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)

    print_a(red)
