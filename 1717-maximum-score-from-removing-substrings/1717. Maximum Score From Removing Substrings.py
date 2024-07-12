class Solution:
    # count the target string
    def cnt(self, s, target):
        res = 0
        st = []
        for ch in s:
            # if encounter the target string
            # by combine current character with previous character
            # in stack
            if st and ch == target[1] and st[-1] == target[0]:
                st.pop()
                res += 1
            else: 
                st.append(ch)
        # also return the remain string after delete target-string
        return res, "".join(st)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0

        # decide which one is high-string 
        # and the remain one is low-string
        hs = "ba" if y > x else "ab"
        ls = "ab" if hs == "ba" else "ba"

        # first turn: count how many high-string
        cnth, nexts = self.cnt(s, hs)

        # second turn: count how many low-string
        cntl, _ = self.cnt(nexts, ls)

        return cnth * max(x, y) + cntl * min(x, y)