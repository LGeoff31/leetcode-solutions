class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        def get_string(num):
            # counts[i] = number of characters currently at letter i (0='a', ..., 25='z')
            counts = [0] * 26
            counts[0] = num
            
            for i in range(25):  # promote a->b->...->y->z (not z, since z doesn't merge away)
                if counts[i] >= 2:
                    pairs = counts[i] // 2
                    counts[i] %= 2
                    counts[i+1] += pairs
            
            
            res = []
            for i in range(25, -1, -1):
                if counts[i] > 0:
                    res.append(chr(ord('a') + i) * counts[i])
            return "".join(res)
        
        return [get_string(n) for n in nums]