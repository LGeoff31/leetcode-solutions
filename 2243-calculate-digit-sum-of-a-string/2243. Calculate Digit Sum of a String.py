class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            k_grouped_s = [s[i : i+k] for i in range(0, len(s), k)]
            new_s = ""
            for group in k_grouped_s:
                new_s += str(sum(int(c) for c in group))
            s = new_s
            print('s', s)
        return s