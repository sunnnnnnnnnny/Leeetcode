class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # record how many vowel words up til from the left
        # time:O(right-left) 
        # space:O(1)
        def isVol(w):
            m = len(w)
            if w[0] in ['a', 'e', 'i', 'o','u'] and w[m-1] in ['a', 'e', 'i', 'o','u']:
                return True
            return False
        now = 0
        for i in range(left, right+1):
            if isVol(words[i]):
                now+=1
        return now