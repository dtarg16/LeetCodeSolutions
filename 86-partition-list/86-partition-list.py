# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode()
        right_head = ListNode()
        left = left_head
        right = right_head
        
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:  
                right.next = head
                right = right.next
            head = head.next
            
        right.next = None 
        left.next = right_head.next 
        return left_head.next  