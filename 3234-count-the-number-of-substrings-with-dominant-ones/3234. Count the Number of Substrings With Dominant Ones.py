class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for k in range(1, int(n**0.5) + 1):
            zeros = deque()
            lastzero = -1
            ones = 0

            for r in range(n):
                if s[r]=="0":
                    zeros.append(r)
                    while len(zeros) > k:
                        ones -= zeros[0] - lastzero - 1
                        lastzero = zeros.popleft()
                else:
                    ones += 1
                if len(zeros) == k and ones >= k**2:
                    res += min(zeros[0] - lastzero, ones - k**2 + 1)
        i = 0
        while i < n:
            if s[i] == "0":
                i += 1
                continue
            length = 0
            while i < n and s[i] == "1":
                length += 1
                i += 1
            res += length * (length + 1) // 2
        return res
