class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        stack = []
        for c in s:
            if c == "[":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    unbalanced += 1
        
        return ceil(unbalanced / 2)