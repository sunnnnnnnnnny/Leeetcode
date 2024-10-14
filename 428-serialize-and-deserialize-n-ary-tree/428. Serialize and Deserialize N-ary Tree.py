"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""
# using open and close bracket making the indication of child
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def preOrder(now, ret):
            if now == None or now.val == None:
                return ret
            ret += str(now.val)+","
            if len(now.children)==0:
                ret += '#'
                return ret
            for ch in now.children:
                ret = preOrder(ch, ret)
            ret += '#'
            return ret
        ans = preOrder(root, "")
        # print(ans)
        return ans
        
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        idx = 0
        def preOrder(data):
            nonlocal idx
            if idx>=len(data):
                return None
            # get current node val
            startIdx = idx
            while idx<len(data):
                if data[idx] == ',':
                    break
                idx += 1
            nowVal = data[startIdx:idx]
            now = Node(int(nowVal), [])
            # print(nowVal,startIdx, idx )
            # no child
            idx+=1
            if idx>=len(data) or data[idx] == '#':
                idx+=1
                return now
            while idx<len(data):
                child = preOrder(data)
                now.children.append(child)
                if data[idx] == '#':
                    idx+=1
                    break
            return now
        
        ret = preOrder(data)
        return ret

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))