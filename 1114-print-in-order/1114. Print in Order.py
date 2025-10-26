from threading import Barrier
class Foo:
    def __init__(self):
        self.b1 = Barrier(2)
        self.b2 = Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b1.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b1.wait()
        printSecond()
        self.b2.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b2.wait()
        printThird()