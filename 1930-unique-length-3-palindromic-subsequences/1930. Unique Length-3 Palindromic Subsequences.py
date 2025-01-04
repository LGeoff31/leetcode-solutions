class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = Counter(s)
        res = 0
        palindromes = set()
        for letter in dic:
            if dic[letter] >= 2:
                first_idx = s.index(letter)
                last_idx = s.rindex(letter)
                for i in range(first_idx+1, last_idx):
                    if letter + s[i] + letter not in palindromes:
                        res += 1
                        # print()
                        palindromes.add(letter + s[i] + letter)
                # res += last_idx - first_idx - 1 # bazab
        return res
