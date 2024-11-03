# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # get one of the path and record it, then checkthe nexy path
        tarPath = set()
        ret = None
        def getNode(now, tar, nowPath):
            nonlocal tarPath, ret
            if now == None:
                return False
            nowPath.append(now)
            if now == tar:
                if len(tarPath) == 0:
                    tarPath = set(nowPath)
                else:
                    for i in range(len(nowPath)-1, -1, -1):
                        n = nowPath[i]
                        if n in tarPath:
                            ret = n
                            break
                return True
            found = getNode(now.left, tar, nowPath)
            if found:
                return found
            found = getNode(now.right, tar, nowPath)
            if found:
                return found
            nowPath.pop()
            return found
        pFound = getNode(root, p, [])
        if not pFound:
            return None
        qFound = getNode(root, q, [])
        return ret