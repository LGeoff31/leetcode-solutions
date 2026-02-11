class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        """
        idea: group as many AB pairs together using stack?
        """
        n = len(seq)
        res = [0] * n
        stack = []

        for i, c in enumerate(seq):
            if c == ")":
                stack.pop()
                res[i] = len(stack) % 2
            else:
                res[i] = len(stack) % 2
                stack.append(c)
        return res