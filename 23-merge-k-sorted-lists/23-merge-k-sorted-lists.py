# Definition for singly-linked https://leetcode.com/problemset/all/list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class PQ:

    def __init__(self):
        self.data = []

    def put(self, priority, element):
        if not self.data:
            self.data.append((priority, element))
        else:
            i = 0
            while i < len(self.data):
                if self.data[i][0] >= priority:
                    break
                i += 1
            self.data.insert(i, (priority, element))

    def get(self):
        if not self.data:
            return None
        ans = self.data[0][1]
        del self.data[0]
        return ans

    def get_length(self):
        return len(self.data)
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        pq = PQ()

        for i in range(len(lists)):
            head = lists[i]
            if head:
                pq.put(head.val, head)
        
        head = pq.get()
        if not head:
            return None
        
        pointer = head
        if head.next:
            pq.put(head.next.val, head.next)
        while pq.get_length() > 0:
            node = pq.get()
            pointer.next = node
            pointer = pointer.next
            if node.next:
                pq.put(node.next.val, node.next)

        return head
        
        