# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:

    def findCelebrity(self, n: int) -> int:
        # check from the lowest index to find if it knows any of the others
        # if x knows y, we will start from y as the next candidate
        # while the people in between x to y knows x, so they are not potential celeb
        # time:O(N+N) = O(N)
        # space:O(1)
        # to save the call to knows using cache, space:O(N)
        nowCand = 0
        cache = {}
        def cacheKnows(x, y):
            nonlocal cache
            if (x,y) not in cache:
                cache[(x,y)] = knows(x,y) 
            return cache[(x,y)]
        for i in range(1,n):
            if cacheKnows(nowCand, i):
                nowCand = i
        # double confirm the candidate doesn't know all the others, and every knows it
        for i in range(n):
            if nowCand != i:
                if cacheKnows(nowCand, i) or not cacheKnows(i, nowCand):
                    return -1
        return nowCand
