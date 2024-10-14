class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 2:
                ans[i] = -1
            else:
                bin_rep = bin(nums[i])[2:]
                idx_leftmost_1 = -1 # Will definitely find a 1
                for j in range(len(bin_rep)-1,-1,-1):
                    if bin_rep[j] == "1":
                        idx_leftmost_1 = j
                    else:
                        break
                # The bit at idx_leftmost_1 must be swapped
                a = list(bin_rep)
                a[idx_leftmost_1] = "0"
                print(a)
                b = "".join(a)
                ans[i] = int(b, 2)
        return ans
