# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node1 = head
        node2 = head
        while node2 is not None and node2.next is not None:
            node1 = node1.next
            node2 = node2.next.next
            if node1 == node2:
                return True
        return False
        