class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dic = Counter(nums)

        res = 0
        def max_elements(base):
            if base == 1:
                return (dic[base]) - (dic[base] % 2 == 0)
            cnt = 0
            if dic[base] == 1:
                return 1
            while True:
                cnt += 2
                base = base ** 2
                if base not in dic:
                    return cnt - 1
                if dic[base] == 1:
                    return cnt + 1 
            return cnt

        for n in dic:
            res = max(res, max_elements(n))

        return max(res,1)