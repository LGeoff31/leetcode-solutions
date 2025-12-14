class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        vowels_count = sum(c in vowels for c in s.split()[0])
        def _vowels(word):
            return sum((c in vowels) for c in word)
        res = [s.split()[0]]
        for word in s.split()[1:]:
            if _vowels(word) == vowels_count:
                res.append(word[::-1])
            else:
                res.append(word)
        return " ".join(res)