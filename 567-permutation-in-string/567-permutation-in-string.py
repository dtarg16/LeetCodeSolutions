class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counter = [0] * 26
        for i in range(len(s1)):
            ch1 = s1[i]
            ch2 = s2[i]
            counter[ord(ch1) - ord('a')] += 1
            if i != len(s1) - 1:
                counter[ord(ch2) - ord('a')] -= 1
                
        for i in range(len(s1)-1, len(s2)):
            ch = s2[i]
            counter[ord(ch) - ord('a')] -= 1
            if i != len(s1) - 1:
                counter[ord(s2[i - len(s1)]) - ord('a')] += 1
            all_zero = True
            for count in counter:
                if count:
                    all_zero = False
            if all_zero:
                return True
        return False