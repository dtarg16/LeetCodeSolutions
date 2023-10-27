class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(map(int, str(n)))
        stack, L = [], len(digits)
        for i in reversed(range(L)):

            if not stack or digits[stack[-1]] <= digits[i]:
                stack.append(i)
                continue

            swapIndex = stack[bisect_right(stack, digits[i], key = lambda x: digits[x])]
            digits[i], digits[swapIndex] = digits[swapIndex], digits[i]
            digits[i+1:L] = sorted(digits[i+1:L])

            break


        nextN = int(''.join(map(str, digits)))
        return nextN if len(stack) < len(digits) and nextN < 2**31 else -1
        
