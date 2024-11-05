# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # do pre-order traversal and put any none existing child as None
        def preOrder(now, retStr):
            if now == None:
                retStr += ",None"
                return retStr
            retStr+= (","+str(now.val))
            retStr = preOrder(now.left, retStr)
            retStr = preOrder(now.right, retStr)
            return retStr
        
        ret = preOrder(root, "")
        # print(ret[1:])
        return ret[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rPreOrderBack(nodeL):
            if nodeL[0] == 'None':
                nodeL.pop(0)
                return None
            now = TreeNode(nodeL[0])
            nodeL.pop(0)
            now.left = rPreOrderBack(nodeL)
            now.right = rPreOrderBack(nodeL)
            return now
        nodeL = data.split(',')
        root = rPreOrderBack(nodeL)
        return root
        # def preOrderBack(nowStr, idx):
        #     if idx >= len(nowStr):
        #         return None, idx
        #     startIdx = idx
        #     while idx<len(nowStr):
        #         if nowStr[idx] == ',':
        #             break
        #         idx+=1
        #     if idx>=len(nowStr):
        #         idx = len(nowStr)
        #     nowNodeStr = nowStr[startIdx:idx]
        #     # print(nowNodeStr, startIdx, idx)
        #     if len(nowNodeStr) == 0 or nowNodeStr == 'None':
        #         return None, idx+1
            
        #     now = TreeNode(int(nowNodeStr))
        #     nowLeft, idx = preOrderBack(nowStr, idx+1)
        #     now.left = nowLeft
        #     nowRight, idx = preOrderBack(nowStr, idx)
        #     now.right = nowRight
        #     return now, idx
        
        # root, endIdx = preOrderBack(data,0)
        # return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))