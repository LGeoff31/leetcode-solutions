class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)

        return word[:idx+len(ch)][::-1] + word[idx+len(ch): ]
        