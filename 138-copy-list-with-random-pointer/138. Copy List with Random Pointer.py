"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # make a mapping from current node to pre node
        # by traverse twice, one time for copy all the node and create mapping
        # second to add the link for update random link
        # time:O(2N) space:O(N)
        old2new = {}
        cur = head
        preHead= pre = Node(1)
        while cur != None:
            newCur = Node(cur.val, None, cur.random)
            old2new[cur] = newCur
            pre.next = newCur
            pre = newCur
            cur = cur.next
        cur = preHead.next
        while cur != None:
            oldRandom = cur.random
            cur.random = old2new[oldRandom] if oldRandom!= None else None
            cur = cur.next
        return preHead.next


        