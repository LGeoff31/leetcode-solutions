class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        """
        You'll get a lot if it follows the format [LARGE, a < b < c < d < e]
        otherwise, you will only get at most 1
        the two largest numbers must be endpoints of the subarr, so you dont have to consider any valid subarr outside that window
        you can then shrink from that window two pointers??!
        monotonic stack?!?
        """
        mono_stack = [] # decending
        valid = 0
        for n in nums:

            while mono_stack and mono_stack[-1] < n:
                mono_stack.pop()
                valid += 1
            valid += len(mono_stack) != 0
            mono_stack.append(n)
        return valid - (len(nums) - 1)