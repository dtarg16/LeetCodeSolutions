class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t) # counter for t to check with
        window = Counter() # sliding window
        ans = "" # answer
        last = 0 # last index in our window
        for i,char in enumerate(s):
            window[char] = window.get(char,0)+1 # add this character to our window
            while window >= tCounter: # while we have all the necessary characters in our window
                if ans == "" or i - last < len(ans): # if the answer is better than our last one
                    ans = s[last:i+1] # update ans
                window[s[last]] -= 1 # remove the last element from our counter
                last += 1 # move the last index forward
        return ans # return answer