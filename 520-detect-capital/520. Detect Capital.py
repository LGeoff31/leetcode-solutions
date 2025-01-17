class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals = 0
        for c in word:
            capitals += c == c.upper()
        if capitals == len(word) or capitals == 0 or capitals == 1 and word[0] == word[0].upper():
            return True
        return False