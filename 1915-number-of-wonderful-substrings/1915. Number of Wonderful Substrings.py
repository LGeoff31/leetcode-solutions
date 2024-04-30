class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}
        freq[0] = 1 #00000 

        mask = 0
        res = 0

        lst = [ord(letter) - ord('a') for letter in word] #aba -> [0,1,0]

        for num in lst:
            mask ^= (1 << num) #0010 
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1
            
            for i in range(10):
                if mask ^ (1 << i) in freq:
                    res += freq[mask ^ (1 << i)] 
        return res

