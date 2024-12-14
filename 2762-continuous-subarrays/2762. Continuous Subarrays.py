class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        idx = 0
        res = 0
        left = 0 
        max_deque = deque()  
        min_deque = deque()  
        
        while idx < len(nums):
            while max_deque and nums[idx] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[idx])
            
            while min_deque and nums[idx] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[idx])
            
            while max_deque[0] - min_deque[0] > 2:
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            
            res += idx - left + 1
            idx += 1
        
        return res
