# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # convert into a graph, then do bfs traversal
        # time:O(2N) space:O(N) to record the graph
        connect = {}
        def dfs(now, par):
            nonlocal connect
            if now == None:
                return
            if now.val not in connect.keys():
                connect[now.val] = []
            if par != None:
                connect[now.val].append(par.val)
                connect[par.val].append(now.val)
            dfs(now.left, now)
            dfs(now.right,now)
        dfs(root, None)
        bfsQ = [target.val]
        level = 0
        visited = set()
        ret = []
        while bfsQ:
            levelSize = len(bfsQ)
            for i in range(levelSize):
                now = bfsQ.pop(0)
                if now in visited:
                    continue
                visited.add(now)
                if level == k:
                    ret.append(now)
                for c in connect[now]:
                    if c not in visited:
                        bfsQ.append(c)
            level+=1
            if level>k:
                break

        return ret
                

