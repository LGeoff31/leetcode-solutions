class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)

        lengths = [0] * n
        cur = 0

        # Forward pass: compute lengths
        for i, c in enumerate(s):

            if 'a' <= c <= 'z':
                cur += 1
            elif c == '*':
                if cur > 0:
                    cur -= 1
            elif c == '#':
                cur *= 2
            else:  # '%'
                pass

            lengths[i] = cur

        if k >= cur:
            return '.'

        # Backward pass
        for i in range(n - 1, -1, -1):
            c = s[i]

            before = 0 if i == 0 else lengths[i - 1]
            after = lengths[i]

            if 'a' <= c <= 'z':
                if k == before:
                    return c
            elif c == '*':
                # All surviving positions keep same index
                continue
            elif c == '#':
                if k >= before:
                    k -= before
            else:  # '%'
                k = after - 1 - k

        return '.'