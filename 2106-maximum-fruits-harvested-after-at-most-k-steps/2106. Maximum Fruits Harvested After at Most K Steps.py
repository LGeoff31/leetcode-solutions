from itertools import accumulate

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # Ensure array large enough to cover startPos ± k
        max_pos = max(max(x for x, y in fruits), startPos + k)
        lst = [0] * (max_pos + 2)
        for x, y in fruits:
            lst[x + 1] = y
        prefix = list(accumulate(lst))  # prefix sum
        startPos += 1  # shift

        res = 0

        # Try going left first
        for left_steps in range(k + 1):
            # After going left_steps left, you have k - 2*left_steps steps to go right
            if k - 2 * left_steps < 0:
                break
            left = startPos - left_steps
            right = startPos + (k - 2 * left_steps)
            left = max(1, left)
            right = min(len(prefix) - 1, right)
            res = max(res, prefix[right] - prefix[left - 1])

        # Try going right first
        for right_steps in range(k + 1):
            # After going right_steps right, you have k - 2*right_steps steps to go left
            if k - 2 * right_steps < 0:
                break
            right = startPos + right_steps
            left = startPos - (k - 2 * right_steps)
            left = max(1, left)
            right = min(len(prefix) - 1, right)
            res = max(res, prefix[right] - prefix[left - 1])

        return res
