import copy

from nonstd.data.__internal import *
from nonstd.data.maybe import Maybe


@dataclass
class List[A]:
    xs: list[A]

    def __init__(self, *xs: Iterable[A]):
        self.xs = list(*xs)

    def __iter__(self):
        return self.xs.__iter__()

    def is_empty(self) -> bool:
        return len(self.xs) == 0

    def is_not_empty(self) -> bool:
        return not self.is_empty()

    def length(self):
        return len(self.xs)

    def head(self):
        return Maybe(self.xs[0])

    def tail(self):
        return List(self.xs[1:])

    def last(self):
        return Maybe(self.xs[-1])

    def map[B](self, f: Callable[[A], B]):
        ys = []
        for x in self.xs:
            ys.append(f(x))
        return List[B](ys)

    def filter(self, f: Callable[[A], bool]):
        ys = []
        for x in self.xs:
            if f(x):
                ys.append(x)
        return List[A](ys)

    def has(self, x: A) -> bool:
        return x in self.xs

    def dict(self):
        d = dict()
        for x in self.xs:
            for k in x.keys():
                d[k] = x[k]
        return d

    def reverse(self):
        ys = copy.copy(self.xs)
        ys.reverse()
        return List(ys)

    def sorted(self, fn):
        ys = copy.copy(self.xs)
        ys.sort(key=fn)
        return ys

    @staticmethod
    def concat[X](xss: "List[List[X]]") -> "List[X]":
        ys = []
        for xs in xss:
            ys.extend(xs)
        return List[X](ys)
