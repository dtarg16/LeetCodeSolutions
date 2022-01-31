class MinStack:

    def __init__(self):
        self.data = []
        self.min_sofar = []

    def push(self, val: int) -> None:
        minn = val if not self.min_sofar else min(val, self.min_sofar[-1])
        self.min_sofar.append(minn)
        self.data.append(val)

    def pop(self) -> None:
        del self.data[-1]
        del self.min_sofar[-1]
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_sofar[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()