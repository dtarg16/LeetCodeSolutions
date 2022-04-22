
class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.data = [None] * 1000
        
    def hash(self, k):
        return k % len(self.data)

    def put(self, key: int, value: int) -> None:
        
        hsh = self.hash(key)
        
        if not self.data[hsh]:
            self.data[hsh] = ListNode(key, value)
        else:
            cur = self.data[hsh]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value) #update
                    return
                if cur.next == None: break
                cur = cur.next
            cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        hsh = self.hash(key)
        cur = self.data[hsh]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        hsh = self.hash(key)
        cur = prev = self.data[hsh]
        if not cur: 
            return
        if cur.pair[0] == key:
            self.data[hsh] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)