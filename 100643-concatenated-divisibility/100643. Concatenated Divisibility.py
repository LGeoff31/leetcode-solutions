class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lengths = [len(str(num)) for num in nums]

        @cache
        def dfs(bit_mask, remainder):
            if bit_mask == (1 << n) - 1:
                if remainder == 0:
                    return []
                return None
            ans = []
            for i in range(n):
                curr_bit = 1 << i
                if bit_mask & curr_bit == 0:
                    # try to use this bit
                    res = dfs(bit_mask | curr_bit, (remainder * 10 ** lengths[i] + nums[i]) % k) # math remainder trick
                    if res is not None:
                        ans.append([nums[i]] + res)
            if not ans:
                return None
            return min(ans)
        return dfs(0, 0) if dfs(0, 0) is not None else []
                        