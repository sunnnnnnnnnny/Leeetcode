# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # as both list are sorted, always take the node from each begining
        # Time: O(N+M) Space:O(1)
        newHead = ListNode()
        parent = newHead
        while list1 and list2:
            nextNode = None
            if list1.val<list2.val:
                nextNode = list1
                list1 = list1.next
            else:
                nextNode = list2
                list2 = list2.next
            parent.next = nextNode
            parent = parent.next
        while list1:
            parent.next = list1
            parent = parent.next
            list1 = list1.next
        
        while list2:
            parent.next = list2
            parent = parent.next
            list2 = list2.next
        return newHead.next