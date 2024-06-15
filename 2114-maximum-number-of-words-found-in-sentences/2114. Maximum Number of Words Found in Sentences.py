class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(arr.split()) for arr in sentences])
        