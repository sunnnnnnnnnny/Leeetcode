# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dp recursive to make it, while loop with var
        # time:O(N) space:O(n) for recursive O(1) for while
        if head is None:
            return head
        prev = None
        cur = head
        while cur!=None:
            nextCur = cur.next
            cur.next = prev
            prev = cur
            cur = nextCur
        return prev








        # # using recursive to get the next node and revert it
        # # also using gobal variable to record the end as the new head
        # # time: O(N) traverse
        # # space: O(N) recrusive taking all the nodes
        # self.oriEndAsNewHead = ListNode(0, None)
        # def getOriChild(self, now, parent):
        #     if not now:
        #         self.oriEndAsNewHead.next = parent
        #         return
        #     getOriChild(self, now.next, now)
        #     now.next = parent
        #     return
        # getOriChild(self, head, None)
        # return self.oriEndAsNewHead.next

        