class LRUCache:

    def __init__(self, capacity: int):
        # record the capacity and the idx of the key to identifty the recent use 
        # alwasy keep the least use in the front, with double linked list
        # or OrderedDict
        self.cap = capacity
        self.key2Val = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.key2Val.keys():
            return -1
        self.key2Val.move_to_end(key)
        return self.key2Val[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.key2Val.keys():
            self.key2Val.move_to_end(key)
            self.key2Val[key] = value
            return 
        if len(self.key2Val) == self.cap:
            self.key2Val.popitem(False)
        self.key2Val[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)