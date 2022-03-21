class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = {}
        for i in range(len(s)):
            ch = s[i]
            last_occur[ch] = i

        parts = []
        i = 0
        while i < len(s):
            ch = s[i]
            start = i
            end = last_occur[ch]
            j = start
            while j < end + 1:
                end = max(end, last_occur[s[j]])
                j += 1

            parts.append(end - start + 1)
            i = end + 1

        return parts