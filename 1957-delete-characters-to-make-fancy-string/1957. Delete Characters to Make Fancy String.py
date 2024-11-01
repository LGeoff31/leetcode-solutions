class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        idx = 0
        while idx < len(s):
            count = 1
            curr = s[idx]
            temp_idx = idx
            while temp_idx+1 < len(s) and s[temp_idx+1] == curr:
                count += 1
                temp_idx += 1
            if count >= 3:
                res += curr + curr
                while idx < len(s) and s[idx] == curr:
                    idx += 1
            else:
                res += curr
                idx += 1
        return res
        