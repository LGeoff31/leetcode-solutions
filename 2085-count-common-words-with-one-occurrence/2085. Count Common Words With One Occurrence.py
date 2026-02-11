class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a,b = Counter(words1), Counter(words2)
        return sum(a[word] == 1 and word in b and b[word] == 1 for word in a)