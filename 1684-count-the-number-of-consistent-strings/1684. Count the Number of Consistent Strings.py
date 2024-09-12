class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            a = 0
            for c in allowed:
                a += word.count(c)
            if a == len(word):
                count += 1
        return count