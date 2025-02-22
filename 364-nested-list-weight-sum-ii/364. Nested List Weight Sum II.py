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
        # aggregate the sum based on the depth, then count it all at the end
        # time:O(N) space:O(N)
        d2Sum = defaultdict(int)
        maxDep = 1
        def getSumInNestIntlist(now, nowDep):
            nonlocal d2Sum, maxDep
            maxDep = max(maxDep, nowDep)
            for i in range(len(now)):
                if now[i].isInteger():
                    d2Sum[nowDep]+=now[i].getInteger()
                else:
                    getSumInNestIntlist(now[i].getList(), nowDep+1)
        getSumInNestIntlist(nestedList, 1)
        ret = 0
        for i in range(1, maxDep+1):
            ret += d2Sum[i]*(maxDep-i+1)
        return ret
            
        