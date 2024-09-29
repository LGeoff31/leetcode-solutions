class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        def atLeast(k):
            n = len(word)
            l, r = 0, 0
            consonant = 0
            dic = {}
            res = 0
            while l < n or r < n:
                if consonant >= k and len(dic) == 5:
                    res += n-r+1
                    if word[l] not in vowels:
                        consonant -= 1
                    else:
                        dic[word[l]] -= 1
                        if dic[word[l]] == 0:
                            del dic[word[l]]
                    l += 1
                else:
                    if r == n: break
                    if word[r] in vowels:
                        dic[word[r]] = 1 + dic.get(word[r], 0)
                    else:
                        consonant += 1
                    r += 1
            return res
        

        return atLeast(k) - atLeast(k+1)