# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse the first time to get the length of list
        # traverse the second time to remove the node
        # time: O(2N) space:O(1)
        # by using 2 pointers, when we get the fast pointer to end
        # the slow pointer is at the middle, thus at most we traverse O(N+N/2)
        if head is None:
            return head
        fast = head
        slow = head
        listLen = 1
        slowIdx = 1
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                listLen+=2
            else:
                if fast.next:
                    listLen+=1
                break
            if slow.next:
                slow = slow.next
                slowIdx+=1
        
        # print(listLen)
        # print(slowIdx)
        # the idx of remove should be len-(n-1)
        removeNodeHead = listLen-n+1
        # print(removeNodeHead)
        newparent = ListNode()
        newparent.next = head
        if removeNodeHead> slowIdx:
            parent = slow
            while slow:
                if removeNodeHead== slowIdx:
                    parent.next = slow.next
                    break
                slowIdx += 1
                parent = slow
                slow = slow.next
        else:
            cur = head
            idx = 1
            parent = newparent
            while cur:
                if removeNodeHead == idx:
                    parent.next = cur.next
                    break
                idx += 1
                parent = cur
                cur = cur.next
        return newparent.next
        


                