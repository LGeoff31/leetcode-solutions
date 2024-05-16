class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []

        dic = Counter(words)
        words = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

        top_k_words = [word for word, freq in words[:k]]
        # top_k_words.sort()
        return top_k_words
        