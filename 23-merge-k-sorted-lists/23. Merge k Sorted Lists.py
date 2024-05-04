# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. brute force take 2 at a time to merge
        # Time: O(N*K) assume ave len is N, total of K list
        # Spae: O(1)
        # 2. using min heap for each start node
        # pop the min heap element each time
        # Time: O(N*logK) Space:O(K) as we need to take all K beging node in queue
        # as each time getting the num from heap cost logK
        kHeads = []
        for idx in range(len(lists)):
            head = lists[idx]
            if head:
                kHeads.append((head.val, idx))
        heapq.heapify(kHeads)
        retHead = ListNode()
        cur = retHead
        while cur and kHeads:
            nextNode = heapq.heappop(kHeads)
            idx = nextNode[1]
            cur.next = lists[idx]
            if lists[idx].next:
                heapq.heappush(kHeads, (lists[idx].next.val, idx))
                lists[idx] = lists[idx].next
            cur = cur.next
        return retHead.next
        