class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = defaultdict(list)
        for i, letter in enumerate(s):
            dic[letter].append(i)
        res=0
        seen = set()
        for letter in dic:
            if len(dic[letter]) >= 2:
                first_idx = dic[letter][0]
                last_idx = dic[letter][-1]
                for i in range(first_idx + 1, last_idx):
                    if letter + s[i] + letter not in seen:
                        seen.add(letter + s[i] + letter)
        return len(seen)

