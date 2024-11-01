from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.allowHy = Semaphore(2)
        self.allowOx = Semaphore(1)
        self.needConntent = Barrier(3)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.allowHy.acquire()
        self.needConntent.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.allowHy.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.allowOx.acquire()
        self.needConntent.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.allowOx.release()