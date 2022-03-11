# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_range(head, left, right):
    prev = None
    current = head
    index = 0
    while index < left:
        prev = current
        current = current.next
        index += 1

    left = prev
    tail = current
    while current and index <= right:
        next = current.next
        current.next = prev
        prev = current
        current = next
        index += 1
    tail.next = current
    if left:
        left.next = prev
    else:
        head = prev
    return head


def length(head):
    ans = 0
    while head:
        ans += 1
        head = head.next
    return ans

class Solution:
    

    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #         head = "------>--->" k =3
        #         result = "--->----->"

        #         reverse "------>--->"   :   "<---<------"
        #         reverse "<---"          :   "---><------"
        #         reverse "<------"       :   "--->------>"
    
        if not head or not head.next:
            return head
        n = length(head)
        k = k % n
        if k == 0:
            return head
        head = reverse_range(head, 0, n - 1)
        head = reverse_range(head, 0, k - 1)
        head = reverse_range(head, k, n - 1)

        return head