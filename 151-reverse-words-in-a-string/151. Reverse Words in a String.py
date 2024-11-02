class Solution:
    def reverseWords(self, s: str) -> str:
        # get the words and insert it in the result
        # time:O(N) space:O(N)
        words = []
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if i>0 and s[i-1]!=' ':
                    nowW = s[start:i]
                    words.insert(0,nowW)
                start = i+1
            else:
                if i == len(s)-1:
                    nowW = s[start:i+1]
                    words.insert(0,nowW)
        return ' '.join(words)