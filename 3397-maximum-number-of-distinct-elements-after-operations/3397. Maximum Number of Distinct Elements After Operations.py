class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Greedy algorithm: Have a visited set. For each num, pick smallest possible avaialble position, if none add unfixable
        nums.sort()
        visited = set()
        nums[0] = nums[0] - k
        prevNum = nums[0]
        visited.add(nums[0])
        unfixable = 0
        for i in range(1, len(nums)):
            if prevNum >= nums[i] + k:
                unfixable += 1
                continue
            found = False
            for num in range(max(prevNum, nums[i] - k), nums[i] + k + 1):
                if num not in visited:
                    visited.add(num)
                    prevNum = num
                    found = True
                    break
            if not found:
                unfixable += 1
        return len(nums) - unfixable
                
                    
                