class LinkN:
    def __init__(self, cnt):
        self.cnt = cnt
        self.val = set()
        self.prev = None
        self.next = None
class AllOne:
# record the key to count and count to key, also keep update the max and min
# time:O(1) for each space:O(N+B) N is the unique keys, B is unique cnt
    def __init__(self):
        self.key2Buck = {}
        self.begin = LinkN(0)
        self.end = LinkN(0)
        self.begin.next = self.end
        self.end.prev = self.begin

    def inc(self, key: str) -> None:
        oriCnt = 0
        buckN = self.begin
        if key in self.key2Buck.keys():
            buckN = self.key2Buck[key]
            oriCnt = buckN.cnt
        # print('inc ', key, oriCnt, buckN.cnt, buckN.val)
        if buckN.next:
            if buckN.next.cnt != oriCnt+1:
                newBuck = LinkN(oriCnt+1)
                newBuck.val.add(key)
                newBuck.prev = buckN
                newBuck.next = buckN.next
                buckN.next.prev = newBuck
                buckN.next = newBuck
                self.key2Buck[key] = newBuck
            else:
                buckN.next.val.add(key)
                self.key2Buck[key] = buckN.next
        if key in buckN.val:
            buckN.val.remove(key)
            if buckN.cnt>0 and len(buckN.val) == 0:
                buckN.prev.next = buckN.next
                buckN.next.prev = buckN.prev
        
    def dec(self, key: str) -> None:
        oriCnt = 0
        buckN = self.end
        if key in self.key2Buck.keys():
            buckN = self.key2Buck[key]
            oriCnt = buckN.cnt
        if buckN.prev:
            if buckN.prev.cnt != oriCnt-1:
                newBuck = LinkN(oriCnt-1)
                newBuck.val.add(key)
                newBuck.prev = buckN.prev
                newBuck.next = buckN
                buckN.prev.next = newBuck
                buckN.prev = newBuck
                self.key2Buck[key] = newBuck
            else:
                if oriCnt-1>0:
                    buckN.prev.val.add(key)
                    self.key2Buck[key] = buckN.prev
                else:
                    del self.key2Buck[key]
        if key in buckN.val:
            buckN.val.remove(key)
            if buckN.cnt>0 and len(buckN.val) == 0:
                buckN.prev.next = buckN.next
                buckN.next.prev = buckN.prev

    def getMaxKey(self) -> str:
        if self.end.prev == self.begin:
            return ""
        maxBuck = self.end.prev
        ret =""
        for a in maxBuck.val:
            ret = a
            break
        return ret
    def getMinKey(self) -> str:
        if self.begin.next == self.end:
            return ""
        minBuck = self.begin.next
        ret =""
        for a in minBuck.val:
            ret = a
            break
        return ret


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()