class WordDictionary:
# need Trie strucutre, if the word is only consisting of alphbet character
# could use # as indication of the end

    def __init__(self):
        self.root = {}
# the time for add is O(M) which is the key length as how far the tree goes
# space is O(M) since we need to add at most the word length
    def addWord(self, word: str) -> None:
        now = self.root
        for i in range(len(word)):
            if word[i] not in now.keys():
                now[word[i]] = {}
            now = now[word[i]]
        now["#"] = True
        
# time for seartch is O(M) b/c it must check all characters until the end to see if exists
# space O(1) as traversing the tree without modification so no extra space
    def search(self, word: str) -> bool:
        def searchRest(nowI, word, head):
            if nowI>=len(word):
                if '#' in head.keys():
                    return True
                return False
            if word[nowI] == '.':
                for key, val in head.items():
                    if key == '#':
                        continue
                    if searchRest(nowI+1, word, head[key]):
                        return True
            if word[nowI] not in head.keys():
                return False
            return searchRest(nowI+1, word, head[word[nowI]])
        
        now = self.root
        return searchRest(0, word, now)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)