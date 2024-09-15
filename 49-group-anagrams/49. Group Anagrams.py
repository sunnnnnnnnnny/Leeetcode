class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the words, and check them as it's the key
        # time:O(n*nlogn) n is the avg len of str
        # space:O(N)
        # go through each str cnt the freq and use it as the key, 
        # group by the key, time:O(n*n) space:O(n)
        # assume the character's only having 36 english character
        # if we consider uppercase letters?
        # also we assume we don't need to deduplicate
        groupKey = {}
        def getK(word):
            keySet = [0 for _ in range(26)]
            for i in range(len(word)):
                char = ord(word[i])-ord('a')
                keySet[char]+=1
            return tuple(keySet)
        for s in strs:
            nowK = getK(s)
            if nowK not in groupKey.keys():
                groupKey[nowK] = []
            groupKey[nowK].append(s)
        return groupKey.values()
