import collections
class FreqStack:

    def __init__(self):
        self.value_freq = collections.Counter()  # counter value frequency
        self.freq_values = collections.defaultdict(list)  # freq -> [val1, val2 .. valn] every val has same frequency
        self.max_freq = 0  # keep track of maximum frequency | if n is no longer max one n-1 should be| xxx then xx

    def push(self, val: int) -> None:
        self.value_freq[val] += 1  # increase counter 
        self.max_freq = max(self.max_freq, self.value_freq[val])  # check if this is new maximum frequency and update
        self.freq_values[self.value_freq[val]].append(val)  # for this freq value update dict so it also contains val

    def pop(self) -> int:
        res = self.freq_values[self.max_freq].pop()  # find list of vals with max frequencies and remove youngest one
        if not self.freq_values[self.max_freq]:  # if there are no more value with this frequency 
            self.max_freq -= 1                   # new highest frequency should be lowered by 1
        self.value_freq[res] -= 1                # update value's frequency counter

        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()