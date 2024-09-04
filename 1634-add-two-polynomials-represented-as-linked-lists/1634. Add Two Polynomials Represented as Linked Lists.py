# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        # simliar to adding two link list, 
        # assume the link list is strickly in the format, thus we can add them based on the power
        # time: O(n+m) space:O(1) no extra space
        newHead = PolyNode()
        prev = newHead
        while poly1 and poly2:
            if poly1.power>poly2.power:
                prev.next = poly1
                poly1 = poly1.next
                prev = prev.next
            elif poly1.power<poly2.power:
                prev.next = poly2
                poly2 = poly2.next
                prev = prev.next
            else:
                tempCo = poly1.coefficient+poly2.coefficient
                # print(tempCo, poly1.power)
                if tempCo != 0:
                    poly1.coefficient = tempCo
                    prev.next = poly1
                    prev = prev.next
                poly1 = poly1.next
                poly2 = poly2.next
                # print(poly1, poly2)
        if poly1:
            prev.next = poly1
        elif poly2:
            prev.next = poly2
        else:
            # need to clear up the next
            prev.next = None
        return newHead.next




        