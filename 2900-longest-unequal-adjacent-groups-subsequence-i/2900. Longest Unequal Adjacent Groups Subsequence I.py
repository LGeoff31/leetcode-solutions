class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = [words[0]]
        prev = groups[0]
        for i in range(1, len(groups)):
            if groups[i] != prev:

                res.append(words[i])
                prev = groups[i]
        return res