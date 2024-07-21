class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        one_count = 0
        segment_started = False
        zero_count = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == "0" and not segment_started:
                segment_started = True
                zero_count += 1
                one_count = 0
            elif s[i] == "1":
                segment_started = False
                while i >= 0 and s[i] == "1":
                    one_count += 1
                    i -= 1
                res += one_count * zero_count
                i += 1
            
            i -= 1
        return res



