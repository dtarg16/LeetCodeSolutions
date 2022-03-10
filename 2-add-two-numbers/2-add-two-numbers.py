# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def number_as_linked_list(self, number):
        last_digit = number % 10
        head = ListNode(last_digit)
        node = head
        while last_digit != number:
            number = number//10
            last_digit = number % 10
            node.next = ListNode(last_digit)
            node = node.next
        return head
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i, j, n1, n2 = 0, 0, 0, 0
        
        while(l1 is not None): 
            n1 += l1.val * pow(10,i)
            l1 = l1.next
            i += 1
        while(l2 is not None): 
            n2 += l2.val * pow(10,j)
            l2 = l2.next
            j += 1
        
        return self.number_as_linked_list(n1 + n2)