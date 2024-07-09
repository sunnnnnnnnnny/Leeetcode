# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # need a map to record the appeared value, 
        # traverse twice, first time remove the duplicate
        # second time remove the first appeared
        # time:O(2N) space:O(2N)
        appearedVal = set()
        duplicateVal = set()
        oriHead = ListNode(next=head)
        pre = oriHead
        cur = head
        while cur!=None:
            if cur.val in appearedVal:
                pre.next = cur.next
                duplicateVal.add(cur.val)
            else:
                pre = cur
                appearedVal.add(cur.val)
            cur = cur.next
        pre = oriHead
        cur = oriHead.next
        while cur!=None:
            if cur.val in duplicateVal:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return oriHead.next


        