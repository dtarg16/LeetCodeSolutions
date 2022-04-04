# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next
        if k == n - k + 1:
            return head
        
        tmp = head
        left, right = None, None
        
        for i in range(1, n + 1):
            if i == k:
                left = tmp
            if i == n - k + 1:
                right = tmp
            
            tmp = tmp.next
        
        #swap
        left.val, right.val = right.val, left.val
        
        return head
        