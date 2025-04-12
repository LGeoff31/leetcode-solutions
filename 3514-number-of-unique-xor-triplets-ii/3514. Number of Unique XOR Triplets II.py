class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums.sort()
        
        # Generate all the pair XOR values in O(n^2), store in hashmap
        # Loop through nums[i] and compare hashmap, so problem becomes XOR a pair
        if len(nums) == 1: return 1
        paired_xor = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                paired_xor.add(nums[i] ^ nums[j])
        ans = set()
        for i in range(len(nums)):
            for b in paired_xor:
                if nums[i] ^ b not in ans:
                    ans.add(nums[i] ^ b)
        return len(ans)