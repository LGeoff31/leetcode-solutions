class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            mini = min(nums[i], nums[-1 - i])
            maxi = max(nums[i], nums[-1 - i])

            delta[2] += 2
            delta[mini + 1] -= 1
            delta[mini + maxi] -= 1
            delta[mini + maxi + 1] += 1
            delta[maxi + limit + 1] += 1

        res = n
        moves = 0

        for targ in range(2, 2 * limit + 1):
            moves += delta[targ]
            res = min(res, moves)

        return res
