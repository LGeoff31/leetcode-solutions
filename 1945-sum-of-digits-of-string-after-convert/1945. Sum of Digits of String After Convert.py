class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a = ""
        for c in s:
            a += str(ord(c) - 96)
        
        for i in range(k):
            a = sum(int(c) for c in str(a))
        return a