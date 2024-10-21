class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, visited):
            if start == len(s):
                return len(visited)
            
            max_splits = 0
            current_substr = ""
            
            for i in range(start, len(s)):
                current_substr += s[i]
                
                if current_substr not in visited:
                    visited.add(current_substr)
                    max_splits = max(max_splits, backtrack(i + 1, visited))
                    visited.remove(current_substr)
            
            return max_splits
        
        return backtrack(0, set())
