class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        dic = Counter(answers)
        for key in dic:
            res += ceil(dic[key] / (key+1)) * (key+1)


        return res