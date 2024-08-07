# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # output the tree as pre-order traversal, with empty node as null string
        # then compare the string, if not then no
        def preOrder(root):
            ret = ""
            bfs = [root]
            while bfs:
                now = bfs.pop(0)
                if now is None:
                    ret += " null"
                else:
                    ret += " "
                    ret+=str(now.val)
                    bfs.append(now.left)
                    bfs.append(now.right)
            return ret
        pStr = preOrder(p)
        qStr = preOrder(q)
        return pStr == qStr
        # traverse the tree in same order and compare
        # yet how to confirm if they are at the same level?
        # adding level form to confirm
        # ex. dfs 0_1 1_2 1_3
        # ex. bfs 1 l 2 3 l
        # time: O(N) space: O(N)
        def getBfsOrder(root: Optional[TreeNode]):
            retStr = ""
            order = deque([root])
            while order:
                levelCnt = len(order)
                for i in range(levelCnt):
                    now = order.popleft()
                    if now == None:
                        retStr += " null"
                        continue
                    retStr += str(now.val)
                    retStr += " "
                    order.append(now.left)
                    order.append(now.right)
                retStr+="l "
            return retStr
        qInStr = getBfsOrder(q)
        pInStr = getBfsOrder(p)
        return qInStr == pInStr