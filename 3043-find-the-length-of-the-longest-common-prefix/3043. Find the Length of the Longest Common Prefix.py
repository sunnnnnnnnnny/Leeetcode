class TrieNum:
    def __init__(self, val):
        self.val = val
        self.child = [None]*10 
        # each node would have at most 0-9 digit child
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # creating the trie by arr1 or arr2, the use every element of the other
        # to find the longest common path
        # time:O(len(arr1)*avg(arr1 length)+len(arr2)*avg(arr2 length))
        # space:O(len(arr1)*(arr1 length))
        toBuildTrie = arr1 if len(arr1)<len(arr2) else arr2
        toSearch = arr2 if len(arr1)<len(arr2) else arr1
        def breakIntoPath(val):
            ret = []
            if val == 0:
                ret.append(val)
                return ret
            while val>0:
                last = val%10
                val = val//10
                ret.append(last)
            # need to reverse it
            return ret[::-1]
        def buildTrie(ret):
            nonlocal startTrie
            prev = startTrie
            now = None
            for i in range(0, len(ret)):
                if prev.child[ret[i]] == None:
                    now = TrieNum(ret[i])
                    prev.child[ret[i]] = now
                prev = prev.child[ret[i]]

        startTrie = TrieNum(0)
        builtSet = set()
        for n in toBuildTrie:
            if n in builtSet:
                continue
            nList = breakIntoPath(n)
            buildTrie(nList)
            builtSet.add(n)
        
        def checkTrie(ret):
            nonlocal startTrie
            prev = startTrie
            commonLen = 0
            for i in range(0, len(ret)):
                if prev.child[ret[i]] == None:
                    break
                commonLen+=1
                prev = prev.child[ret[i]]
            return commonLen
        checkSet = set()
        maxCommonLen = 0
        for n in toSearch:
            if n in checkSet:
                continue
            nList = breakIntoPath(n)
            cLen = checkTrie(nList)
            checkSet.add(n)
            maxCommonLen = max(maxCommonLen, cLen)
        return maxCommonLen
        


