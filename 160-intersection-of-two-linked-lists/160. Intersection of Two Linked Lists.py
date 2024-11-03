# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # keep a hash of the node, then go through it, time:O(N+M) space:O(N)
        # 2 pointers, with getting the start at same length of each list
        def getLength(node):
            if node.next == None:
                return 1, node
            nowLen, endN = getLength(node.next)
            return nowLen+1, endN
        aLen, aEnd = getLength(headA)
        bLen, bEnd = getLength(headB)
        if aEnd != bEnd:
            return None
        commonLen = min(aLen, bLen)
        print(commonLen)
        aNow = headA
        aIdx = 0
        while aLen-aIdx>commonLen:
            aNow = aNow.next
            aIdx += 1
        bNow = headB
        bIdx = 0
        while bLen-bIdx>commonLen:
            bNow = bNow.next
            bIdx += 1   
        while aNow!=bNow:
            aNow = aNow.next
            bNow = bNow.next
        return aNow