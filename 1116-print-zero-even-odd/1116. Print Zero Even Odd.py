from threading import Lock
class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.is_odd = True
        self.z = Lock()
        self.e = Lock()
        self.o = Lock()
        self.e.acquire()
        self.o.acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.o.release()
            else:
                self.e.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()
        