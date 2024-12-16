# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # need to know how len and round down, then use the left to add one to use
        # time:O(2N) = O(N) space:O(N)
        totalLen = 0
        now = head
        while now:
            now = now.next
            totalLen += 1
        eachSize = totalLen//k
        left = totalLen%k
        ret = []
        prev = None
        now = head
        for _ in range(k):
            batchS = eachSize
            if left>0:
                batchS += 1
                left -= 1
            # nowRet = []
            # if now:
            #     nowRet.append(now)
            ret.append(now)
            if prev:
                prev.next = None
            for _ in range(batchS):
                if now == None:
                    break
                prev = now
                now = now.next
            # ret.append(nowRet)
        return ret
            