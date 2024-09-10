
class TreNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False
class Trie:
    def __init__(self):
        # record if the child and it's self is an leaf node
        self.root = TreNode()

    def insert(self, word: str) -> None:
        now = self.root
        for i in range(len(word)):
            if word[i] not in now.child.keys():
                now.child[word[i]] = TreNode()
            now = now.child[word[i]]
            if i==len(word)-1:
                now.isEnd = True

    def search(self, word: str) -> bool:
        now = self.root
        for i in range(len(word)):
            if word[i] in now.child.keys():
                now = now.child[word[i]]
                if i==len(word)-1:
                    return now.isEnd
            else:
                return False
        return False
        

    def startsWith(self, prefix: str) -> bool:
        now = self.root
        for i in range(len(prefix)):
            if prefix[i] in now.child.keys():
                now = now.child[prefix[i]]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)