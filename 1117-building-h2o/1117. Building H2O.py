class H2O:
    def __init__(self):
        self.bar = threading.Barrier(3)
        self.h2Lock = threading.Semaphore(2)
        self.oLock = threading.Semaphore(1)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h2Lock.acquire()
        self.bar.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h2Lock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oLock.acquire()
        self.bar.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oLock.release()