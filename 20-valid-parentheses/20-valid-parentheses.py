class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = list()
        
        for ch in s:
            if not stack:
                stack.append(ch)
            else:
                if ch in left:
                    stack.append(ch)
                else:
                    top = stack.pop()
                    if top in right or left.index(top) != right.index(ch):
                        return False
        return not stack