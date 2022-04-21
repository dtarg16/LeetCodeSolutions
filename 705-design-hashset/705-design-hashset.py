class MyHashSet:

    def __init__(self):
        self.len = 16
        self.data = [0] * self.len
        

    def add(self, key: int) -> None:
        while self.len < key + 1:
            self.data += [0] * self.len
            self.len *= 2
        self.data[key] = 1
    
    def remove(self, key: int) -> None:
        if key < self.len:
            self.data[key] = 0

    def contains(self, key: int) -> bool:
        if key < self.len:
            return self.data[key] == 1
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)