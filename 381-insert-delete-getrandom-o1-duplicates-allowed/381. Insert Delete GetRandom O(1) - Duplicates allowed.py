from random import choice
class RandomizedCollection:
# array for random, with dict for keeping the idx
    def __init__(self):
        self.cnt = defaultdict(set)
        self.lst = []

    def insert(self, val: int) -> bool:
        ret = True
        if val in self.cnt.keys():
            ret = False
        idx = len(self.lst)
        self.cnt[val].add(idx)
        self.lst.append(val)
        return ret

    def remove(self, val: int) -> bool:
        ret = False
        if val in self.cnt.keys():
            ret = True
            idx = self.cnt[val].pop()
            # swap the remove idx with the last idx
            swapVal = self.lst[-1]
            self.lst[idx] = swapVal
            self.lst.pop()
            self.cnt[swapVal].add(idx)
            self.cnt[swapVal].remove(len(self.lst))
            if len(self.cnt[val]) == 0:
                del self.cnt[val]
        return ret

    def getRandom(self) -> int:
        return choice(self.lst)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()