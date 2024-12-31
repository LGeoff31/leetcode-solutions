class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows, cols = len(words), len(words[0])
        for i in range(max(rows, cols)):
            a = words[i]
            b = ""
            for word in words:
                if i < len(word):
                    b += word[i]
            if a != b: return False
        return True