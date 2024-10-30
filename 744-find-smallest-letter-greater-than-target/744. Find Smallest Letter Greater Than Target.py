class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # could use binary search for getting the largest
        def conver2Idx(c):
            # print(ord('a'))
            return (ord(c[0])-ord('a'))
        targetIdx = conver2Idx(target)
        left = 0
        minC = conver2Idx(letters[left])
        if minC>targetIdx:
            return letters[0]
        right = len(letters)-1
        maxC = conver2Idx(letters[right])
        if maxC<=targetIdx:
            return letters[0]
        while left<=right:
            mid = (left+right)//2
            midIdx = conver2Idx(letters[mid])
            if midIdx>targetIdx:
                right = mid-1
            else:
                left = mid+1
        return letters[left]