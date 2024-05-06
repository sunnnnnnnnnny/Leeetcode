class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # By adding the counts of character in s
        # then check if all the character appeared the same freq in t
        # time: O(s+t) as we would explore the whole s and t string
        # space: O(s) as we keep record max of all the char in s
        # method 2, by sorting the s and t to compare them
        # time: O(NlogN) space: O(1)
        if len(s)!=len(t):
            return False
        # by utilizing the counter of python
        from collections import Counter 
        return Counter(s) == Counter(t)
        # sChar = {}
        # for i in range(len(s)):
        #     if s[i] not in sChar:
        #         sChar[s[i]] = 0
        #     sChar[s[i]] += 1
        
        # for i in range(len(t)):
        #     if t[i] not in sChar:
        #         return False
        #     sChar[t[i]] -= 1
        #     if sChar[t[i]] == 0:
        #         del sChar[t[i]]
            
        # return True


        