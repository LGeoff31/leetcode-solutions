class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        curr = 1
        i = len(weight) - 2
        res = 0
        min_so_far = weight[-1]
        for i in range(len(weight) -2, -1, -1):
            if weight[i] > min_so_far:
                res += 1
                if i == 0:
                    break
                min_so_far = weight[i-1]
            else:
                min_so_far = weight[i]
        return res