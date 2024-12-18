class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [] # Increasing

        for i, num in enumerate(nums):
            while stack and num < stack[-1] and len(nums) - i > k - len(stack):
                stack.pop()
            stack.append(num)
        return stack[:k]