# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def length(self, head):
        counter = 0
        while head:
            head=head.next
            counter += 1
        return counter
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lengthA = self.length(headA)
        lengthB = self.length(headB)
        nodeA = headA
        nodeB = headB
        
        # difference in total length is difference before intersection
        
        if lengthB < lengthA:
            for i in range(lengthA - lengthB):
                nodeA = nodeA.next
                
        if lengthA < lengthB:
            for i in range(lengthB - lengthA):
                nodeB = nodeB.next
                
        while nodeA:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
            
        return None