class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        """
        Clearly, the ending nums must be sorted.
        so the q' becomes what is the minimum number of swaps to make this a sorted array
        basically a bubbling algorithm
        """
        number_elements_below_a = sum(n < a for n in nums)
        number_elements_between_a_and_b = sum(a <= n <= b for n in nums)
        number_elements_above_b = sum(n > b for n in nums)
        res = 0
        cur = 0
        idx_a = [i for i in range(len(nums)) if nums[i] < a]
        idx_b = [i for i in range(len(nums)) if a <= nums[i] <= b]
        idx_c = [i for i in range(len(nums)) if nums[i] > b]
        c1,c2,c3 =0,0,0
        for i in range(len(nums)):
            if nums[i] < a:
                res += c2+c3
                c1 += 1
            elif nums[i] <= b:
                res += c3
                c2+=1
            else:
                c3 += 1
            
        return res % MOD
        
        # print(idx_a, idx_b, idx_c)
        # for idx in idx_a:
        #     res += idx - cur
        #     cur += 1
        # for idx in idx_b:
        #     res += idx - cur
        #     cur += 1
        # for idx in idx_c:
        #     res += idx - cur
        #     cur += 1
        
        # return res
        
        
        