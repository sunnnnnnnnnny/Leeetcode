# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive getting the double num of the later char
        # and return the carrier over from child
        # time: O(N) as all node needs to be traverse
        # space:O(N) the stack will go at most depth of O(N)
        def doubleChild(cur):
            if cur==None:
                return 0
            carrier = doubleChild(cur.next)
            newVal = cur.val*2+carrier
            cur.val = int(newVal%10)
            return int(newVal/10)
        headCarrier = doubleChild(head)
        if headCarrier==0:
            return head
        newHead = ListNode()
        newHead.val = headCarrier
        newHead.next = head
        return newHead
        