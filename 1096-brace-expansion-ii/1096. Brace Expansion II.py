class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.i = 0

        def concat(a, b):
            return {x + y for x in a for y in b}

        def parse_expr():
            res = {""}

            while self.i < len(self.s) and self.s[self.i] not in "},":
                if self.s[self.i] == "{":
                    cur = parse_brace()
                else:
                    cur = {self.s[self.i]}
                    self.i += 1

                res = concat(res, cur)

            return res

        def parse_brace():
            # Skip '{'
            self.i += 1

            res = set()

            while True:
                part = parse_expr()
                res |= part

                if self.s[self.i] == ",":
                    self.i += 1
                else:
                    break

            self.i += 1

            return res

        ans = parse_expr()
        return sorted(ans)