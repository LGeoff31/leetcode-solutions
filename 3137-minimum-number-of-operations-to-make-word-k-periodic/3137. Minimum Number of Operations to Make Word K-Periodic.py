class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        dic = {}

        for i in range(0, len(word), k):
            substring = word[i:i+k]
            dic[substring] = 1 + dic.get(substring, 0)
        
        max_freq = max(dic.values())
        return (len(word) - max_freq * k) //k

        