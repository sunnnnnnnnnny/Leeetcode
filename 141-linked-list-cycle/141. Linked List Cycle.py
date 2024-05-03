# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force, keep a dictionary of all the nodes
        # if any node appeared twice, then detected cycle
        # time: O(N), space: O(N)
        # 2 pointers of fast and slow, with fast being at the speed of 2
        # if fast = slow, meaning there's a cycle
        # Time: O(2N)=O(N) space:O(1)
        if not head:
            return False
        fast = head.next
        slow = head
        while fast:
            if fast == slow:
                return True
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                break
            if slow.next:
                slow = slow.next
        return False
        