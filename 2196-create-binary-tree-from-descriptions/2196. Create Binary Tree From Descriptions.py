# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # root will be only appearing in parent, compare node and child
        # time:O(2N) space:O(N)
        n2Node = {}
        child = set()
        for des in descriptions:
            par, ch, isLeft = des
            if par not in n2Node.keys():
                now = TreeNode(par)
                n2Node[par] = now
            if ch not in n2Node.keys():
                now = TreeNode(ch)
                n2Node[ch] = now
            if isLeft == 1:
                n2Node[par].left = n2Node[ch]
            else:
                n2Node[par].right = n2Node[ch]
            child.add(ch)
        for n in n2Node.keys():
            if n not in child:
                return n2Node[n]
        return None

        # count the edge connected as constrait, then we can get the root and build it
        # time: O(2N) space:O(N)
        # num2Par = defaultdict(list)
        # num2ParEdge = defaultdict(int)
        # root = set()
        # for des in descriptions:
        #     par, ch, isLeft = des
        #     num2Par[par].append(des)
        #     num2ParEdge[ch] += 1
        #     if num2ParEdge[par] == 0:
        #         root.add(par)
        #     if ch in root:
        #         root.remove(ch)
        # # expect valid binary tree should only have one root
        # actRoot = None
        # for x in root:
        #     now = TreeNode(x)
        #     nextQ = [(x,now)]
        #     while nextQ:
        #         level = len(nextQ)
        #         for i in range(level):
        #             nowN, parNode = nextQ.pop(0)
        #             # get child
        #             for chList in num2Par[nowN]:
        #                 par, ch, isLeft = chList
        #                 nextCh = TreeNode(ch)
        #                 if isLeft == 1:
        #                     parNode.left = nextCh
        #                 else:
        #                     parNode.right = nextCh
        #                 nextQ.append((ch, nextCh))

        #     actRoot = now 
        # return actRoot