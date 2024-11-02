# from threading import lock
import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.Q= []
        self.p_lock = threading.Lock()

    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        self.p_lock.acquire()
        self.Q.append(element)
        self.p_lock.release()
        self.pulling.release()

    def dequeue(self) -> int:
        self.pulling.acquire()
        self.p_lock.acquire()
        ret = self.Q.pop(0)
        self.p_lock.release()
        self.pushing.release()
        return ret

    def size(self) -> int:
        ret = len(self.Q)
        return ret