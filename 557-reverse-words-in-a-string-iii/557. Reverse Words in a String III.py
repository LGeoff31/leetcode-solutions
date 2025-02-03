class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        for word in s.split():
            lst.append(word[::-1])
        return " ".join(lst)