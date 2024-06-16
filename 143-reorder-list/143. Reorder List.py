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
        # using the fast and slow pointer, then with slow one revert the par-child
        # and connect with the slow point moving foward link the points
        # time: O(N) spance:O(1)
        fast = slow = head
        preParent = None
        while fast:
            if slow.next != None:
                preParent = slow
                slow = slow.next
            if fast.next != None and fast.next.next!=None:
                fast = fast.next.next
            else:
                break
        # to avoid having none with only one item
        if preParent != None:
            preParent.next = None
        preParent = None
        # reverse the second part
        while slow:
            tempSlow = slow.next
            slow.next = preParent
            preParent = slow
            slow = tempSlow
        # print(preParent)
        first = head
        while preParent != None:
            tempFirst = first.next
            tempSec = preParent.next
            first.next = preParent
            preParent.next = tempFirst
            first = tempFirst
            preParent = tempSec
        # brute force traverse the list and put in list, 
        # directly using their idx for reorder
        # time:O(2N) space:O(N) for new list
        # nodeList = []
        # cur = head
        # while cur:
        #     nodeList.append(cur)
        #     cur = cur.next
        # left = 0
        # right = len(nodeList)-1
        # newParent = ListNode()
        # parent = newParent
        # while left<=right:
        #     parent.next = nodeList[left]
        #     parent = parent.next
        #     if left<right:
        #         parent.next = nodeList[right]
        #         parent = parent.next
        #     parent.next = None
        #     left +=1
        #     right -=1
        # return newParent.next



        