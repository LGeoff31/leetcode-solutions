class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = {}
        freq[0] = 1
        mask, res = 0, 0
        lst = [ord(letter) - ord("a") for letter in word]

        for num in lst:
            mask ^= (1 << num) #a -> 0001, b -> 0010
            if mask in freq:
                res += freq[mask] #0010, 0010 
                freq[mask] += 1
            else:
                freq[mask] = 1
            
            for i in range(10): #a -> j
                if mask ^ (1 << i) in freq:
                    res += freq[mask ^ (1 << i)]
        return res
