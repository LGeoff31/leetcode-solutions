class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for letter in jewels:
            res += stones.count(letter)
        return res