# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # can calculate the sum of all int, and also record the 
        # minus parts, then getting the result as (maxDep+1)*sum-minus part
        # bfs: time;O(N) space:O(1)
        maxDep = 1
        curDep = 1
        totalSum = 0
        deducted = 0
        bfsQ = nestedList
        while bfsQ:
            levelSize = len(bfsQ)
            for i in range(levelSize):
                now = bfsQ.pop(0)
                if now.isInteger():
                    totalSum += now.getInteger()
                    deducted += curDep*now.getInteger()
                else:
                    bfsQ.extend(now.getList())
            curDep += 1
        maxDep = curDep-1
        # print(maxDep, totalSum, deducted)
        posPart = (maxDep+1)*totalSum
        ret = posPart - deducted
        return ret