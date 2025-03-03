class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        seen = set() # 5, 6, 2, 0, 4, 1, 3
        max_length = 0 # 4

        #[5,4,0,3,1,6,2] 

        for n in nums:
            # 3
            if n not in seen:
                length = 0
                while n not in seen: # length = 1
                    length += 1
                    seen.add(n)
                    n = nums[n]
                max_length = max(max_length, length)

        return max_length