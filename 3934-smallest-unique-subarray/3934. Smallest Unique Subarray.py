class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        """
        If there's any single unique element, the answer is 1.

        Rolling hash: 
        [1,34,5,7,8,10], length = 2

        1st term: 1 * 31^(6) + 34 * 31^5
        2nd term: 
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        B = 12345

        def valid(length):
            seen = set()
            counter = defaultdict(int)

            rolling_hash = sum(nums[i-1] * (pow(B, length - i, MOD)) for i in range(1, length + 1)) % MOD
            counter[rolling_hash] += 1

            for i in range(1, len(nums) - length + 1):
                rolling_hash = ((rolling_hash - (nums[i-1] * (pow(B, length - 1, MOD)))) * B + nums[i + length - 1]) % MOD
                counter[rolling_hash] += 1

            return any(counter[key] == 1 for key in counter)

        l, r = 1, len(nums)
        res = float('inf')

        while l <= r:
            trial_length = (l + r) // 2

            if valid(trial_length):
                r = trial_length - 1
                res = min(res, trial_length)
            else:
                l = trial_length + 1
        
        return res
