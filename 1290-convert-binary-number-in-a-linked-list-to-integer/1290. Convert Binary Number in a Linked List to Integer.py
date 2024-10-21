# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # making the reverse of it
        num = 0
        def getNext(now):
            nonlocal num
            if now == None:
                return 1
            smallSec = getNext(now.next)
            nowN = now.val * smallSec
            num += nowN
            return smallSec*2
        getNext(head)
        return num