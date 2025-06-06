from threading import Barrier
from threading import Semaphore

class H2O:
    def __init__(self):
        self.sem_h = Semaphore(2)
        self.sem_o = Semaphore(1)
        self.barrier = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.sem_h:
            self.barrier.wait()
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.sem_o:
            self.barrier.wait()
            # releaseOxygen() outputs "O". Do not change or remove this line.
            releaseOxygen()