class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        dic = {0: 1}
        for num in nums:
            curr_sum += num
            mod = curr_sum % k
            if mod < 0:
                mod += k
            if mod in dic:
                res += dic[mod]
            dic[mod] = 1 + dic.get(mod, 0)
            # print(res, dic)
        return res