import copy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m -= 1
        n -= 1
        curr_idx = m + n + 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[curr_idx] = nums1[m]
                m -= 1
            else:
                nums1[curr_idx] = nums2[n]
                n -= 1
            curr_idx -= 1
        #fill in whats remaining of non-empty array


        while n >= 0:
            nums1[curr_idx] = nums2[n]
            n -= 1
            curr_idx -= 1
        
        
