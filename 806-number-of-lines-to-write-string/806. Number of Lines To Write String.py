class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        number_of_lines, current_allocation = 1, 0

        for c in s:
            w = widths[ord(c) - ord('a')]
            if w + current_allocation > 100:
                # Take it over to the next line
                number_of_lines += 1
                current_allocation = w
            else:
                current_allocation += w 
        
        return [number_of_lines, current_allocation]