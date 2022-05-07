class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = float('-inf')
        st = []
        for num in reversed(nums):
            if num < s3:
                return True
            else:
                while st and num > st[-1]:
                    s3 = st.pop()
            
            st.append(num)
            
        return False