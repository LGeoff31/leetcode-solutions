class Solution:
    def canAliceWin(self, n: int) -> bool:
        a = 10
        alice = True
        while True:
            if n - a < 0:
                return not alice
            n -= a
            a -= 1
            alice = not alice
        