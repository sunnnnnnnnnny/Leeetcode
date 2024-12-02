class LinkN:
    def __init__(self, cnt):
        self.cnt = cnt
        self.val = set()
        self.preN = None
        self.nextN = None
class AllOne:
# time:O(1) space:O(N+bucket)
    def __init__(self):
        self.head = LinkN(0)
        self.tail = LinkN(0)
        self.head.nextN = self.tail
        self.tail.preN = self.head
        self.v2Buk = {}

    def inc(self, key: str) -> None:
        # print("start inc")
        buk = self.head
        newCnt = 1
        if key in self.v2Buk:
            buk = self.v2Buk[key]
            buk.val.remove(key)
            newCnt = buk.cnt+1
            # print("ince", key, newCnt)
            
            if len(buk.val) == 0:
                temp = buk.preN
                buk.preN.nextN = buk.nextN
                buk.nextN.preN = buk.preN
                buk = temp
        # print(key, newCnt)
        if buk.nextN.cnt == newCnt:
            buk.nextN.val.add(key)
            self.v2Buk[key] = buk.nextN
        else:
            # print("inc:", key, newCnt)
            newBuk = LinkN(newCnt)
            buk.nextN.preN = newBuk
            newBuk.nextN  = buk.nextN
            buk.nextN = newBuk
            newBuk.preN = buk
            newBuk.val.add(key)
            self.v2Buk[key] = newBuk
        nowBuk = self.v2Buk[key]
        # if nowBuk.preN !=None:
        #     print(nowBuk.preN.cnt)
        # if nowBuk.nextN !=None:
        #     print(nowBuk.nextN.cnt)
        # print("finish inc")


    def dec(self, key: str) -> None:
        if key not in self.v2Buk:
            return
        buk = self.v2Buk[key]
        newCnt = buk.cnt-1
        buk.val.remove(key)
        if len(buk.val) == 0:
            temp = buk.nextN
            buk.preN.nextN = buk.nextN
            buk.nextN.preN = buk.preN
            buk = temp
        if newCnt == 0:
            del self.v2Buk[key]
            return
        if buk.preN.cnt == newCnt:
            buk.preN.val.add(key)
            self.v2Buk[key] = buk.preN
        else:
            newBuk = LinkN(newCnt)
            buk.preN.nextN = newBuk
            newBuk.preN  = buk.preN
            buk.preN = newBuk
            newBuk.nextN = buk
            newBuk.val.add(key)
            self.v2Buk[key] = newBuk

    def getMaxKey(self) -> str:
        ket = self.tail.preN.val
        for i in ket:
            return i
        return ""

    def getMinKey(self) -> str:
        ket = self.head.nextN.val
        for i in ket:
            return i
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()