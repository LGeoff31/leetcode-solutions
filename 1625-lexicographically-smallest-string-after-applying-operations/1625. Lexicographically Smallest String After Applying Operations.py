class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        How many shifts until we reach a cycle?
        lcm(b, len(s))
        abc -> bca -> cab -> abc
        b = 3
        lcm(2, 3) = 6

        """
        visited = set()
        # visited.add(s)
        queue = deque([s])
        res = "9" * len(s)
        while queue:
            w = list(queue.popleft())
            res = min(res, "".join(w))
            for j in range(10):
                word = w.copy()
                for k in range(len(word)):
                    if k % 2 == 1:
                        word[k] = str((int(word[k]) + a ) % 10 )
                if "".join(word) not in visited:
                    visited.add("".join(word))
                    queue.append(word)
            new_s = w[len(w) - b : ] + w[:-b]
            if "".join(new_s) not in visited:
                visited.add("".join(new_s))
                queue.append(new_s)
        return res
           