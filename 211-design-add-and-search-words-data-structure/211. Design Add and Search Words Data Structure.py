class WordDictionary:

    def __init__(self):
        self.mtDict = {}
# the time for add is O(M) which is the key length as how far the tree goes
# space is O(M) since we need to add at most the word length
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
# time for seartch is O(M) b/c it must check all characters until the end to see if exists
# space O(1) as traversing the tree without modification so no extra space
    def search(self, word: str) -> bool:
        def checkChild(self, nowDict, leftWord):
            if len(leftWord) == 0:
                if '#' in nowDict.keys():
                    return True
                return False
            key = leftWord[0]
            # need to avoid the ending key
            if key == '.':
                for anyKey in nowDict.keys():
                    if anyKey != '#' and checkChild(self, nowDict[anyKey], leftWord[1:]):
                        return True
            if key in nowDict:
                return checkChild(self, nowDict[key], leftWord[1:])
            return False
        return checkChild(self, self.mtDict,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)