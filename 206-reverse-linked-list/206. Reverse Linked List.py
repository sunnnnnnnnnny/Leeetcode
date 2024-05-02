# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using recursive to get the next node and revert it
        # also using gobal variable to record the end as the new head
        # time: O(N) traverse
        # space: O(N) recrusive taking all the nodes
        self.oriEndAsNewHead = ListNode(0, None)
        def getOriChild(self, now, parent):
            if not now:
                self.oriEndAsNewHead.next = parent
                return
            getOriChild(self, now.next, now)
            now.next = parent
            return
        getOriChild(self, head, None)
        return self.oriEndAsNewHead.next

        