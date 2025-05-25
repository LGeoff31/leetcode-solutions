class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        words_set = set(words)
        dic=Counter(words)
        used = set()
        odd_used = False
        for word in words:
            if word in used:
                continue
            if word[0] == word[1]:
                if dic[word] > 1:
                    if odd_used:
                        res += dic[word] * 2 if dic[word] % 2 == 0 else (dic[word]-1) * 2
                    else:
                        res += dic[word] * 2
                        odd_used = dic[word] % 2 == 1
                elif not odd_used:
                    res += 2
                    odd_used = True
                used.add(word)
            else:
                if word[::-1] in words_set:
                    res += min(dic[word], dic[word[::-1]]) * 4
                    used.add(word)
                    used.add(word[::-1])
        return res

                