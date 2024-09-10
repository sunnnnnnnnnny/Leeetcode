# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bydoing preorder or postorder we could see if the subroot is in the tree
        # also in order to have the correct child, we need to print delimieter for it
        # time: O(N+M+N) traversal both tree takes, N and M
        # the time to find the substring is O(N)
        # spaceL:O(N+M) as we need the postOrder of both trees
        def postOrder(now):
            if now == None:
                return "# "
            left = postOrder(now.left)
            right = postOrder(now.right)
            return left+right+str(now.val)+" "
        rootPostOrder = postOrder(root)
        subPostOrder = postOrder(subRoot)
        # print(rootPostOrder)
        # print(subPostOrder)
        # print(rootPostOrder.find(subPostOrder))
        return rootPostOrder.find(subPostOrder)>=0
        # do the traverse of root then compare each node to subroot
        # brute force: time= O(M*N) space:O(M+N)
        # serialize both trees, then check if subtree is the substring
        # by adding null as empty indicator for the preorder / postorder
        # time: O(M+N) space: O(M+N)
        # def preOrder(now:Optional[TreeNode]):
        #     preStr = ""
        #     trav = deque()
        #     trav.append(now)
        #     while trav:
        #         levelCnt = len(trav)
        #         for i in range(levelCnt):
        #             cur = trav.popleft()
        #             if cur == None:
        #                 preStr += "Null "
        #                 continue
        #             trav.append(cur.left)
        #             trav.append(cur.right)
        #             preStr += str(cur.val)
        #             preStr += " "
        #     return preStr
        # rootStr = preOrder(root)
        # subStr = preOrder(subRoot)
        # return rootStr.find(subStr)
            
        