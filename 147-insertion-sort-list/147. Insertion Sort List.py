# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # how to quickly identify the insert location
        # time:O(N^2) space:O(1)
        if head == None:
            return head
        newHead = ListNode()
        # newHead.next = head
        now = head
        idx=1
        while now:
            prev = newHead
            # print("start:", idx,now.val)
            while prev.next and prev.next.val<=now.val:
                prev = prev.next
            # print(idx, prev.val, now.val)
            temp = now.next
            now.next = prev.next
            prev.next = now
            now = temp
            idx += 1
            pNow = newHead.next
            # for i in range(idx):
            #     print(i,pNow.val)
            #     pNow = pNow.next
        return newHead.next

