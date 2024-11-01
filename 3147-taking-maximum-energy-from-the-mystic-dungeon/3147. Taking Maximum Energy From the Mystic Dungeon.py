class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = [-1e9] * len(energy)
        dp[-1] = energy[-1]

        for i in range(len(energy) -2, -1, -1):
            if i + k < len(energy):
                dp[i] = energy[i] + dp[i+k]
            else:
                dp[i] = energy[i]
        return max(dp)