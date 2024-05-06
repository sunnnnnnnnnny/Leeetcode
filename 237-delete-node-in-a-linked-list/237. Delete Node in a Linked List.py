# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # correct is to remove the node of next one
        # node->node.next.next
        # time: O(1) space:O(1)
        node.val = node.next.val
        node.next = node.next.next
        # we are not removing the node of link
        # but by taking the child val and remove the last node linkage
        # TIME:O(N) as we go through all nodes
        # space:O(N) need to record the next val
        def replacePreVal(cur, pre):
            if cur.next != None:
                nextVal = cur.next.val
                replacePreVal(cur.next, cur)
                cur.val = nextVal
            else:
                pre.next = None
        # replacePreVal(node, None)
            


        
        