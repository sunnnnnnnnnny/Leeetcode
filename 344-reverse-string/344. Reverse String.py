class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # need a temp str to do the swap
        # doing it on both ends, Time: O(n/2), space: O(1)
        left = 0
        right = len(s)-1
        
        while left<right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -=1
        

        