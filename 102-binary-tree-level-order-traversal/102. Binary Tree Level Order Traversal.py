# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # do bfs traversal to print each level 
        # with adding left to right into the queue
        # time: O(N) space: O(N) 
        # the space could be O(1) cause it's binary tree thus not that much node
        # can be access at once
        ret = []
        traverse = deque()
        traverse.append(root)
        while traverse:
            levelCnt = len(traverse)
            levelList = []
            for i in range(levelCnt):
                now = traverse.popleft()
                if now == None:
                    continue
                traverse.append(now.left)
                traverse.append(now.right)
                levelList.append(now.val)
            if len(levelList)>0:
                ret.append(levelList)
        return ret

        