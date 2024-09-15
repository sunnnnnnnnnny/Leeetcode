# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # go through the list together and add any carry one
        if l1 == None or l2 == None:
            return l1 if l1 is not None else l2
        preHead = ListNode()
        preHead.next = l1
        carryOver = 0
        prev = preHead
        while l1 and l2:
            nowVal = l1.val + l2.val + carryOver
            if nowVal>=10:
                carryOver = 1
                nowVal = nowVal%10
            else:
                carryOver = 0
            l1.val = nowVal
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l1 != None or l2 != None:
            now = l1 if l1 is not None else l2
            prev.next = now
            while now and carryOver>0:
                nowVal = now.val + carryOver
                if nowVal>=10:
                    carryOver = 1
                    nowVal = nowVal%10
                else:
                    carryOver = 0
                now.val = nowVal
                prev = now
                now = now.next
        if carryOver>0:
            endN = ListNode(val=1)
            prev.next = endN



        return preHead.next