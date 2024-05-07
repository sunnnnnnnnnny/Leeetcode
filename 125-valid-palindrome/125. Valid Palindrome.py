class Solution:
    def isPalindrome(self, s: str) -> bool:
        # go through the str to remove none letter and lower case 
        # then check either from the middle or the end for each char of validation
        # Time: O(2N)
        # Space: O(N) to record the valid letters
        # 2. check from start and end with pointer
        # then skip none letters
        # Time: O(N), space:O(1) for 2 pointers
        start = 0
        end = len(s)-1
        s = s.lower()
        while start<end:
            if start == end:
                break
            # using isalnum to check if the character is alphanumeric
            if not s[start].isalnum():
                start += 1
                continue
            
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            

        