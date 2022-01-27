class Solution:
    root = dict()
    n = 0

    def build_trie(self, nums):
        self.root = dict()
        self.n = len(bin(max(nums))[2::]) + 1
        for num in nums:
            node = self.root
            for i in reversed(range(self.n)):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = dict()

                node = node[bit]

    def find_max_for_current(self, num):
        node = self.root
        target_num = 0
        for i in reversed(range(self.n)):
            bit = (num >> i) & 1
            target_bit = 0 if bit else 1
            if target_bit in node:

                target_num = target_num * 2 + target_bit
                node = node[target_bit]
            else:
                target_num = target_num * 2 + bit
                node = node[bit]

        return target_num
    
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        self.build_trie(nums)

        maxx = 0
        for num in nums:
            max_for_num = self.find_max_for_current(num)
            if max_for_num ^ num > maxx:
                print(num, max_for_num)
            maxx = max(maxx, max_for_num ^ num)

        return maxx