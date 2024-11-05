class Bucket:
    def __init__(self):
        self.bucket = []
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1
    def update(self, key, val):
        found = False
        for i in range(len(self.bucket)):
            k, v = self.bucket[i]
            if k == key:
                self.bucket[i] = (key, val)
                found = True
                break
        if not found:
            self.bucket.append((key, val))
    def remove(self, key):
        found = False
        retI = -1
        for i in range(len(self.bucket)):
            k, v = self.bucket[i]
            if k == key:
                retI = i
                found = True
                break
        if found:
            del self.bucket[i]
class MyHashMap:

    def __init__(self):
        # better to be a prime, less collision
        self.keySpace = 2069
        self.hashTable = [Bucket() for i in range(self.keySpace)]

    def put(self, key: int, value: int) -> None:
        hashKey = key%self.keySpace
        self.hashTable[hashKey].update(key, value)
        

    def get(self, key: int) -> int:
        hashKey = key%self.keySpace
        return self.hashTable[hashKey].get(key)

    def remove(self, key: int) -> None:
        hashKey = key%self.keySpace
        self.hashTable[hashKey].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)