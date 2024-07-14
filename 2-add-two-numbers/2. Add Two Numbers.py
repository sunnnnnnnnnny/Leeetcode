# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # take the carry
        # time: O(N)
        carryOne = 0
        cur1 = l1
        cur2 = l2
        ret = ListNode()
        ret.next = cur1
        pre = ret
        while cur1 != None and cur2!=None:
            newVal = cur1.val+cur2.val+carryOne
            carryOne = newVal//10
            newVal = newVal%10
            cur1.val = newVal
            pre = cur1
            cur1 = cur1.next
            cur2 = cur2.next
        if cur2!=None:
            pre.next = cur2
            cur1 = cur2
        while carryOne>0 and cur1 != None:
            newVal = cur1.val+carryOne
            carryOne = newVal//10
            newVal = newVal%10
            cur1.val = newVal
            pre = cur1
            cur1 = cur1.next
        if carryOne>0:
            newNode = ListNode(carryOne)
            pre.next = newNode
        return ret.next


        