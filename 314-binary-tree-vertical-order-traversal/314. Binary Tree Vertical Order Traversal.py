# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs with preorder traversal, and keep track of the vertical cnt
        # time:O(2N) space:O(N)
        if root == None:
            return []
        row2Keys = {}
        minRow = maxRow = 0
        # bfs
        checkNext = [(root, 0)]
        while checkNext:
            levelCnt = len(checkNext)
            for i in range(levelCnt):
                now, row  = checkNext.pop(0)
                if now.left!=None:
                    checkNext.append((now.left,row-1))
                if now.right!=None:
                    checkNext.append((now.right,row+1))
                if row not in row2Keys.keys():
                    row2Keys[row] = []
                row2Keys[row].append(now.val)
                minRow = min(minRow, row)
                maxRow = max(maxRow, row)
        # get back the ret by sorted row
        ret = []
        for i in range(minRow, maxRow+1):
            ret.append(row2Keys[i])
        return ret
        