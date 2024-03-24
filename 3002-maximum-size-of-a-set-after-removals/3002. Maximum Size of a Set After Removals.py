import collections
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        max_len = len(nums1) // 2
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        if len(nums1_set) <= max_len and len(nums2_set) <= max_len:
            return len(nums1_set.union(nums2_set))
        
        num1_added = set()

        for num in nums1_set:
            if num not in nums2_set and len(num1_added) < max_len:
                num1_added.add(num)
        
        num2_added = set()
        
        for num in nums2_set:
            if num not in nums1_set and len(num2_added) < max_len:
                num2_added.add(num)
    
        for i in nums1_set:
            if len(num1_added) < max_len and i not in num1_added:
                num1_added.add(i)
        
        for i in nums2_set:
            if len(num2_added) < max_len and i not in num1_added and i not in num2_added:
                num2_added.add(i)
        
        return len(num1_added.union(num2_added))
        
        
        
        
        