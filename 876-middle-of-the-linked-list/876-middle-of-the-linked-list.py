# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node1 = head
        node2 = head
        while node2 is not None and node2.next is not None:
            node1 = node1.next
            node2 = node2.next.next
        return node1
        