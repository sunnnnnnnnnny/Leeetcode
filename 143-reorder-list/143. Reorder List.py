# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # brute force traverse the list and put in list, 
        # directly using their idx for reorder
        # time:O(2N) space:O(N) for new list
        nodeList = []
        cur = head
        while cur:
            nodeList.append(cur)
            cur = cur.next
        left = 0
        right = len(nodeList)-1
        newParent = ListNode()
        parent = newParent
        while left<=right:
            parent.next = nodeList[left]
            parent = parent.next
            if left<right:
                parent.next = nodeList[right]
                parent = parent.next
            parent.next = None
            left +=1
            right -=1
        return newParent.next



        