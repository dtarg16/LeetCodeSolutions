class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        maxx = 0
        index = 0
        while index < len(heights):
            height = heights[index]

            if len(stack) == 0 or heights[stack[-1]] <= height:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()

                width = index
                if len(stack) > 0 == 0:
                    width = index - stack[-1] - 1

                area = width * heights[top_of_stack]
                maxx = max(maxx, area)

        while len(stack) > 0:
            top_of_stack = stack.pop()

            width = index
            if len(stack) > 0 == 0:
                width = index - stack[-1] - 1

            area = width * heights[top_of_stack]
            maxx = max(maxx, area)

        return maxx
        