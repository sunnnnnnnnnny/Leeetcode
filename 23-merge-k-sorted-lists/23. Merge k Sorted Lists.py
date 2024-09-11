# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force way go through each list head everytime
        # better is to use a min heap to pop out the min of all list head
        # heap size is O(K), pop and insert takes O(logK)
        # assume all item size O(N), time: O(NlogK) space :O(K) if not consider the return
        minHeap = []
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(minHeap, (lists[idx].val, idx))
        
        head = ListNode()
        prev = head
        while minHeap:
            now = heapq.heappop(minHeap)
            prev.next = lists[now[1]]
            prev = prev.next
            if lists[now[1]].next != None:
                lists[now[1]] = lists[now[1]].next
                heapq.heappush(minHeap, (lists[now[1]].val, now[1]))
        return head.next
