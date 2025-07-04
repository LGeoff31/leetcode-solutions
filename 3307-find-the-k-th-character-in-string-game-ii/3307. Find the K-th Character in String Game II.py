class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Let k = 2^l + a
        if a = 0, i.e k=4, then we need (l-1) operations ans: last charcter
        if a != 0, i.e k=5, then we need l operations ans: (a-1)th character on lth level
        """
        ans = 0
        while k > 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))