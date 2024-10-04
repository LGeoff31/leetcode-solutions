class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        l,r = 0, len(skills) - 1
        skills.sort()
        target_sum = skills[l] + skills[r]
        res = 0
        while l < r:
            if skills[l] + skills[r] != target_sum:
                return -1 
            res += skills[l] * skills[r]
            l += 1
            r -= 1
        return res
        

        