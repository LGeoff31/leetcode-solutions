class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        a = prod(nums)

        res = 0
        cnt = 2
        while a != 1:
            found = False
            while a % cnt == 0:
                a //= cnt
                found = True
            res += found
            cnt += 1
            print(res, cnt )

        return res