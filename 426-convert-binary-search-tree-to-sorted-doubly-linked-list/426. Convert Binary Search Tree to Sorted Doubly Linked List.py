"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # do twice of he in order, then post order we wil get the link
        # map the original node then make it
        if root == None:
            return None
        first, last = None, None
        def dfsIn(now):
            nonlocal first, last
            if now == None:
                return
            dfsIn(now.left)
            if last != None:
                last.right = now
                now.left = last
            else:
                first = now
            last = now
            dfsIn(now.right)
            return
        dfsIn(root)
        last.right = first
        first.left = last
        return first