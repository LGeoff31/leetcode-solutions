class Solution:
    def countRotations(self, s: str, k: int) -> int:
        cyclic = []

        for i in range(len(s)):
            cyclic.append(s)
            s = s[1:] + s[0]

        res = 0
        for word in cyclic:
            cnt = 0
            for i in range(len(word) - 1):
                cnt += word[i] == word[i+1]
            if cnt == k:
                res += 1
        print(cyclic)
        return res
