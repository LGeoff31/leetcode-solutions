class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        dic = Counter(nums)
        for i in range(len(moveFrom)):
            if moveFrom[i] == moveTo[i]:
                continue
            dic[moveTo[i]] = dic[moveFrom[i]] 
            del dic[moveFrom[i]]
            # print(dic)
        res = set()
        for key in dic:
            res.add(key)
        return sorted(list(res))