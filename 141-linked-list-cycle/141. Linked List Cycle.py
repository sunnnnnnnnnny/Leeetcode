# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # brute force is adding all the visited node in a hashmap, 
        # once find existed node, meaning theres a cycle
        # time:O(N) as hashSet check is O(1), space:O(N) for hashset
        # better way is fast&slow poineter, 
        # fast goes 2 steps, and slow goes 1, then at a certain point if slow==fast
        # cycle detected, if fast == None, no cycle
        # time:O(2N)=:(N) space:O(1)
        slow = fast = head
        while fast!=None:
            fast = fast.next
            if fast!=None:
                fast = fast.next
            else:
                break
            slow = slow.next
            if fast == slow:
                return True
        return False
        # hashSet = set()
        # cur = head
        # while cur!=None:
        #     if cur in hashSet:
        #         return True
        #     hashSet.add(cur)
        #     cur = cur.next
        # return False