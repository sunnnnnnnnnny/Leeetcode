import threading
class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.push = threading.Lock()
        self.pull = threading.Lock()
        self.Q = []
        self.pull.acquire()

    def enqueue(self, element: int) -> None:
        self.push.acquire()
        self.Q.append(element)
        if self.pull.locked():
            self.pull.release()
        if len(self.Q)<self.cap:
            self.push.release()

    def dequeue(self) -> int:
        self.pull.acquire()
        ret = self.Q.pop(0)
        if self.push.locked():
            self.push.release()
        if len(self.Q)>0:
            self.pull.release()
        return ret

    def size(self) -> int:
        return len(self.Q)