# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = right = left = ListNode(0, head)
        for i in range(n):
            left = left.next
        
        while left.next:
            left = left.next
            right = right.next
            
        right.next = right.next.next
        return dummy.next
