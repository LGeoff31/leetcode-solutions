class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        k %= sum(chalk)
        while True:
            if k < chalk[i]:
                return i
            k -= chalk[i]
            i = (i+1) % len(chalk)
            # print(i, k)

        