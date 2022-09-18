class Solution:
    def trap(self, height: List[int]) -> int:
        walls = {}
        dec_mono_stack = []
        
        for i, v in enumerate(height):
            while dec_mono_stack and v > height[dec_mono_stack[-1]]:
                mid_index = dec_mono_stack.pop()
                if not dec_mono_stack:
                    # no left wall, can't trap
                    break
                left_wall_i = dec_mono_stack[-1]
                right_wall_i = i
                height_val = min(height[left_wall_i], height[right_wall_i]) - height[mid_index]
                walls[(left_wall_i, right_wall_i)] = height_val * (right_wall_i - left_wall_i - 1)
                
            dec_mono_stack.append(i)
                
        return sum(walls.values())