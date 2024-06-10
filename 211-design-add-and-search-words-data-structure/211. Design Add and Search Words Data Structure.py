class WordDictionary:

    def __init__(self):
        self.mtDict = {}

    def addWord(self, word: str) -> None:
        # use space to get the search
        # always expand the word by having it as Trie
        def addChild(self, nowDict, leftWord):
            if len(leftWord) == 0:
                # indicating the end
                nowDict['#'] = {}
                return
            key = leftWord[0]
            if key not in nowDict:
                nowDict[key] = {}
            return addChild(self, nowDict[key],leftWord[1:])
        return addChild(self, self.mtDict,word)
    def search(self, word: str) -> bool:
        def checkChild(self, nowDict, leftWord):
            if len(leftWord) == 0:
                if '#' in nowDict.keys():
                    return True
                return False
            key = leftWord[0]
            if key == '.':
                for anyKey in nowDict.keys():
                    if checkChild(self, nowDict[anyKey], leftWord[1:]):
                        return True
            if key in nowDict:
                return checkChild(self, nowDict[key], leftWord[1:])
            return False
        return checkChild(self, self.mtDict,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)