class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        """
        edge case: numbers triplet zeros
        binary search??
        list of Counters, right[i] denotes count all numbers + frequency from i -> end and left is vice versa
        """
        MOD = 10 ** 9 + 7
        l = defaultdict(int)
        l[nums[0]] += 1
        r = defaultdict(int)
        for i in range(2, len(nums)):
            r[nums[i]] += 1
        res = 0
        for i in range(1, len(nums) - 1):
            val = nums[i]
            if 2*val in l and 2*val in r:
                res += l[2*val] * r[2*val]
            l[nums[i]] += 1
            r[nums[i+1]] -= 1
            if r[nums[i+1]] == 0:
                del r[nums[i+1]]
        return res % MOD
           

            
            
        
        