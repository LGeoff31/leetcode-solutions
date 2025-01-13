class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        l,r = 0, 0
        queue = deque([])
        dic = defaultdict(int)
        while r < len(word):
            if queue and word[r] < queue[-1]:
                queue = deque([word[r]])
                dic = defaultdict(int)
                dic[word[r]] += 1
            else:
                queue.append(word[r])
                dic[word[r]] += 1
            if len(dic) == 5:
                res = max(res, len(queue))
            r += 1
        return res