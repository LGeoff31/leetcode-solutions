class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        a,b = 0, 0
        player_one_active = True
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                player_one_active = not player_one_active
            if (i+1) % 6 == 0:
                player_one_active = not player_one_active
            if player_one_active:
                a += nums[i]
            else:
                b += nums[i]
        return a-b