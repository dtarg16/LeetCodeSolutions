class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []    
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(line)
                line = [word]
                line_length = len(word)
        
        result.append(line)
        
        justified_lines = []
        
        for i in range(len(result) - 1):
            line = result[i]
            num_words = len(line)
            num_spaces = maxWidth - sum(len(word) for word in line)
            
            space_gaps = max(num_words - 1, 1)
            
            spaces_per_gap = num_spaces // space_gaps
            extra_spaces = num_spaces % space_gaps

            justified_line = ""
            
            for word in line:
                justified_line += word
                
                if space_gaps > 0:
                    spaces_to_add = spaces_per_gap + (1 if extra_spaces > 0 else 0)
                    justified_line += " " * spaces_to_add
                    extra_spaces -= 1
                    space_gaps -= 1

            justified_lines.append(justified_line)

        last_line = " ".join(result[-1])
        last_line += " " * (maxWidth - len(last_line))
        justified_lines.append(last_line)

        return justified_lines