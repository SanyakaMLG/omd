from typing import TypeVar, Sequence, Callable, Generator, Type

T = TypeVar('T')


class Seq:
    def __init__(self, sequence: Sequence[T] = None, generator: Generator = None):
        if sequence is not None:
            self.generator = (val for val in sequence)
        else:
            self.generator = generator

    def filter(self, predicate: Callable[[T], bool]):
        def inner_filter():
            for v in self.generator:
                if predicate(v):
                    yield v

        return Seq(generator=inner_filter())

    def map(self, func: Callable):
        def inner_map():
            for v in self.generator:
                yield func(v)

        return Seq(generator=inner_map())

    def take(self, count: int):
        res = []
        it = iter(self.generator)
        i = 0
        while i < count:
            try:
                res.append(next(it))
            except StopIteration:
                break
            i += 1

        return res


if __name__ == '__main__':
    s = Seq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    arr = (
        s.filter(lambda x: x % 2 == 0)
        .filter(lambda x: x > 5)
        .map(str)
        .filter(lambda x: len(x) > 1)
        .take(4)
    )
    print(arr)
