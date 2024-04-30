class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}
        freq[0] = 1
        mask = 0
        res = 0
        lst = [ord(x) - ord("a") for x in word]
        print(lst)
        for i in range(len(lst)):
            mask ^= (1 << lst[i])
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            
            for j in range(0, 10):
                if mask ^ (1 << j) in freq:
                    res += freq[mask ^ (1 << j)]
        return res