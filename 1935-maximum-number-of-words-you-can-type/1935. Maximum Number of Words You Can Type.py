class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a = set(brokenLetters)
        res = 0
        for word in text.split():
            valid = True
            for c in word:
                if c in a:
                    valid = False
            if valid:
                res += 1
        return res