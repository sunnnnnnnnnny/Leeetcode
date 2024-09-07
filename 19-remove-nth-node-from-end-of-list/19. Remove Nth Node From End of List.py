# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # having the 2 pointer n step difference, then when fast pointer reachedd
        # the end, the slow end would landed on the removed part's parent
        # time:O(N) space:O(1)
        fast = head
        slow = ListNode()
        slow.next = head
        newHead = slow
        for i in range(n):
            fast = fast.next
        while fast!=None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return newHead.next
        
        
        
        
        
        # # brute force way is going through all to get the length, 
        # # and will get the right index on second iteration , time:O(2N) space:O(1)
        # # 2 pointers, having the fast to end faster, then slow could be in the middle
        # # thus the time may be faster but still O(N)
        # # hashmap to record the index and directly remove once find the end
        # # time:O(N) space:O(N)
        # slow = fast = head
        # newHead = ListNode()
        # newHead.next = head
        # prev = newHead
        # lenCnt = 0
        # slowIdx= 0
        # while fast!=None:
        #     if fast.next:
        #         fast = fast.next.next
        #         lenCnt +=2
        #     else:
        #         fast = fast.next
        #         lenCnt +=1
        #     prev = slow
        #     slow = slow.next
        #     slowIdx+=1
        # removeIdx = lenCnt-n
        # if removeIdx<slowIdx:
        #     slowIdx = 0
        #     slow = head
        #     prev = newHead
        # # print(lenCnt, slowIdx, removeIdx)
        # while slowIdx<=removeIdx:
        #     if slowIdx==removeIdx:
        #         prev.next = slow.next
        #     prev = slow
        #     slow = slow.next
        #     slowIdx+=1
        # return newHead.next