# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # if knowing someone, then it's not the candidate
        # get the only candidate, and exam it
        # time:O(N) space:O(1)
        def isCele(cand,n):
            for i in range(n):
                if i!=cand:
                    if knows(cand, i) or not knows(i, cand):
                        return False
            return True
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
        if isCele(cand,n):
            return cand
        return -1
        # count the incoming edges, ask knows all the other people 
        # record the out going and incoming edge
        # time:O(N^2) space:O(2N)
        # inE = [0]*n
        # outE = [0]*n
        # for i in range(n):
        #     for j in range(n):
        #         if i!=j:
        #             if knows(i,j):
        #                 outE[i] += 1
        #                 inE[j] += 1
        # for i in range(n):
        #     if outE[i] == 0 and inE[i] == n-1:
        #         return i
        # return -1