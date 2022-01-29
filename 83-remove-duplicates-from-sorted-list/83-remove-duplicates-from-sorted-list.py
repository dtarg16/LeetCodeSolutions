# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr and curr.next:
            if curr.next.val == curr.val:

                if curr == head:
                    head = head.next
                    curr = head
                else:
                    curr = curr.next
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head