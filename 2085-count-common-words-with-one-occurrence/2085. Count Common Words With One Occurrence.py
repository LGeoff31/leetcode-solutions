class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return sum(Counter(words1)[word] == 1 and word in Counter(words2) and Counter(words2)[word] == 1 for word in Counter(words1))