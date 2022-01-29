# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reverse(self, head):
        if head is None or head.next is None:
            return head
        
        rest = self.reverse(head.next)
        
        head.next.next = head
        head.next = None
        
        return rest
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        right = self.reverse(slow)
        left = head
        while right:
            if right.val != left.val:
                return False
            right = right.next
            left = left.next
        return True
        
        
        