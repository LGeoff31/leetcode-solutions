class Solution:
    def removeKdigits(self, nums: str, k: int) -> str:
        stack = []
        for i in range(len(nums)):
            while stack and k and stack[-1] > nums[i]:
                stack.pop()
                k -= 1
            if stack or nums[i] is not "0":
                stack.append(nums[i])
        
        if not stack or k >= len(stack): return "0"
        
        return "".join(stack[0:len(stack) - k])

        


        


        


