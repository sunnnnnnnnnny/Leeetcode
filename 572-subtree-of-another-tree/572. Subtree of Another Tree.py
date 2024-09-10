# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # by comparing the root and subroot, we need to find the subRoot
        # only if both node exist in same direct will it be subtree
        ret = False
        def compare2Tree(now, sub):
            if now == None and sub == None:
                return True
            if now == None or sub == None:
                return False
            if  now.val != sub.val:
                return False
            return compare2Tree(now.left, sub.left) and compare2Tree(now.right, sub.right) 
            
        def dfsCompare(now, subroot):
            nonlocal ret
            if now == None and subroot == None:
                ret = True
                return
            if now == None or subroot == None:
                return
            
            if now.val == subroot.val:
                if compare2Tree(now, subroot):
                    ret = True
            dfsCompare(now.left, subroot)
            dfsCompare(now.right, subroot)
        dfsCompare(root, subRoot)
        return ret
            