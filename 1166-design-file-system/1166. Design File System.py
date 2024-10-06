class FileSystem:
# making like a Trie structure, so we know how to creat it
    def __init__(self):
        # store the value as (val, {})
        self.path = {}

    def createPath(self, path: str, value: int) -> bool:
        route = path.split('/')
        # print(route)
        if len(route) == 1:
            return False
        now = self.path
        for i in range(1,len(route)-1):
            if route[i] not in now.keys():
                return False
            else:
                now = now[route[i]]["child"]
        if route[-1] in now.keys():
            return False
        now[route[-1]] = {"val":value, "child":{}}
        return True

    def get(self, path: str) -> int:
        route = path.split('/')
        if len(route) == 1:
            return -1
        now = self.path
        ret = -1
        for i in range(1,len(route)):
            if route[i] not in now.keys():
                ret = -1
                break
            else:
                ret = now[route[i]]["val"]
                now = now[route[i]]["child"]
        return ret
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)