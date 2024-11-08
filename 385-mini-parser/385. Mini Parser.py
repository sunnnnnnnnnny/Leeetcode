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
    def deserialize(self, s: str) -> NestedInteger:
        # go from left 2 right, eventime a [ is adding a nest
        # a valid input is only being the a single NestedInteger
        # time:O(len(s)) space:O(nestedList)
        if s[0] != '[':
            return NestedInteger(int(s))
        prev = 0
        ret = NestedInteger()
        holder = [ret]
        for i in range(len(s)):
            if s[i] == '[':
                now = NestedInteger()
                if len(holder)>0:
                    holder[-1].add(now)
                holder.append(now)
                prev = i+1
            elif s[i] == ',':
                nowS = s[prev:i]
                # print(i, nowS)
                if len(nowS)>0:
                    nowInt = NestedInteger(int(nowS))
                    inside = holder[-1]
                    inside.add(nowInt)
                prev = i+1
            elif s[i] == ']':
                nowS = s[prev:i]
                # print(']',i, nowS)
                if len(nowS)>0:
                    nowInt = NestedInteger(int(nowS))
                    # print(nowInt.getInteger())
                    inside = holder[-1]
                    inside.add(nowInt)
                holder.pop()
                prev = i+1
        first = ret.getList()
        return first[0]
        