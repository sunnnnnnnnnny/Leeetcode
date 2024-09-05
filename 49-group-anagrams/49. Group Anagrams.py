class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # since the character is fixed to 26 english ones, we can use the count of each as the key
        # time:O(n*m) space:O(n*m)
        # convert the str to sorted and use it as key to gather the group
        # time: O(n*mlogm) space:O(n*m) for the key
        keyGroup = {}
        for s in strs:
            c = [0]*26
            for i in range(len(s)):
                cIdx = ord(s[i])-ord('a')
                c[cIdx]+=1

            k = tuple(c)
            # k = ''.join(sorted(s))
            if k not in keyGroup.keys():
                keyGroup[k] = []
            keyGroup[k].append(s)
        ret = keyGroup.values()
        return ret













        # # by counting the anagram of each words as key
        # # then group the words by key
        # # time: O(NK) for counting the key, K is the max len of str
        # # space: O(NK) record the keys, max length of the list length+word length
        # # 2. sort the words as the key, then group it
        # # time: O(NKlog(K)) Space:O(NK)
        # ans: DefaultDict[int, List[str]] = collections.defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord('a')]+=1
        #     ans[tuple(count)].append(s)
        # return ans.values()
        # # thie is sort thus time cost higher
        # # anaGroup = {}
        # # from collections import Counter
        # # for eachStr in strs:
        # #     key = ''.join(sorted(eachStr))
        # #     if key not in anaGroup:
        # #         anaGroup[key] = []
        # #     anaGroup[key].append(eachStr)
        # # return anaGroup.values()

        