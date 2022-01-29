# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr, prev = head, None
        
        while curr:
            if curr.val == val:
                # need to delete current node
                if curr == head:
                    head = head.next 
                    curr = head
                else:
                    curr = curr.next
                    prev.next = curr

            else:
                # go next
                prev = curr
                curr = curr.next

        return head
        