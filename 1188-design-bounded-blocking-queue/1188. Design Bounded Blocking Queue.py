import threading
class BoundedBlockingQueue(object):
# 2 ways , with 2 locks and record the capacity
# another way is to use semaphore of size capacity with one read lock
    def __init__(self, capacity: int):
        self.Q = []
        self.cap = capacity
        self.wLock = threading.Lock()
        self.rLock = threading.Lock()
        self.rLock.acquire()

    def enqueue(self, element: int) -> None:
        self.wLock.acquire()
        self.Q.append(element)
        if len(self.Q)<self.cap:
            self.wLock.release()
        if self.rLock.locked():
            self.rLock.release()

    def dequeue(self) -> int:
        self.rLock.acquire()
        ret = self.Q.pop(0)
        if len(self.Q)>0:
            self.rLock.release()
        if self.wLock.locked():
            self.wLock.release()
        return ret

    def size(self) -> int:
        return len(self.Q)
        