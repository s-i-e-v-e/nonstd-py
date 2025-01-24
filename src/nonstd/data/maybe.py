from nonstd.data.__internal import *

@dataclass
class Maybe[T]:
    _value: T|None

    def __init__(self, value: 'T|None'):
        self._value = value

    @staticmethod
    def nothing() -> 'Maybe[T]':
        return Maybe(None)

    def is_just(self) -> bool:
        return not self.is_nothing()

    def is_nothing(self) -> bool:
        return self._value is None

    def just(self, default: T|None = None) -> T:
        if default is not None:
            return self._value if self.is_just() else default
        elif self.is_nothing():
            raise ValueError("Attempted to unwrap a Nothing value.")
        else:
            return self._value

    def map[U](self, fn: Callable[[T], U]) -> 'Maybe[U]':
        return Maybe[U](fn(self._value)) if self.is_just() else Maybe.nothing()

    def bind[U](self, fn: Callable[[T], U]) -> 'Maybe[U]':
        return fn(self._value) if self.is_just() else Maybe.nothing()