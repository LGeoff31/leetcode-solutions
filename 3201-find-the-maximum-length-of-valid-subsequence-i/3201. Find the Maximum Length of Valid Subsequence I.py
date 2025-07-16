class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # In the subsequence, it must follow all pairs have odd sum or even sum
        # For all odd sum, must be odd + even or even + odd
        # For all even sum, must be even + even or odd + odd

        res = 0 
        # Consider all even numbers
        even = sum([num%2==0 for num in nums])

        # Consider all odd numbers
        odd = sum([num%2 for num in nums])

        # Consider odd then even, alternating
        odd_then_even = 0
        odd_turn = True
        for i in range(len(nums)):        
            if odd_turn:
                if nums[i] % 2:
                    odd_then_even += 1
                    odd_turn = not odd_turn
            else:
                if nums[i]%2 == 0:
                    odd_then_even += 1
                    odd_turn = not odd_turn
        # Consider even then odd, alternating
        even_then_odd = 0
        even_turn = True
        for i in range(len(nums)):
            if even_turn:
                if nums[i] % 2 == 0:
                    even_then_odd += 1
                    even_turn = not even_turn
            else:
                if nums[i] % 2:
                    even_then_odd += 1
                    even_turn = not even_turn
        return max(even,odd, odd_then_even, even_then_odd)

