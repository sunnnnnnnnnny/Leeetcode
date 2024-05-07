class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # by counting the anagram of each words as key
        # then group the words by key
        # time: O(N) for counting the key
        # space: O(N) record the keys, max length of the list length+word length
        # 2. sort the words as the key, then group it
        # time: O(Nlog(N)) Space:O(N)
        anaGroup = {}
        from collections import Counter
        for eachStr in strs:
            key = ''.join(sorted(eachStr))
            if key not in anaGroup:
                anaGroup[key] = []
            anaGroup[key].append(eachStr)
        ret = []
        for key in anaGroup:
            ret.append(anaGroup[key])
        return ret

        