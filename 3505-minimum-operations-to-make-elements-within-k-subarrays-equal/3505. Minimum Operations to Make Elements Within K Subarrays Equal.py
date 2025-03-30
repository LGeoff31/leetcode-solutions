class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
            
        left = SortedList([nums[0]])
        right = SortedList(nums[1:x])
        left_sum = sum(left)
        right_sum = sum(right)
        
        def balance():
            nonlocal left_sum
            nonlocal right_sum
            
            while len(right) < x // 2:
                val = left.pop()
                left_sum -= val
                right.add(val)
                right_sum += val
                
            while len(right) > x // 2:
                val = right[0]
                del right[0]
                left.add(val)
                left_sum += val
                right_sum -= val

            while left[-1] > right[0]:
                val = left.pop()
                right.add(val)
                left_sum -= val
                right_sum += val

                val = right[0]
                del right[0]
                left.add(val)
                left_sum += val
                right_sum -= val
        
        balance()        

        middle_location = left[-1]
        left_cost = middle_location * len(left) - left_sum
        right_cost = right_sum - middle_location * len(right)
        cost = left_cost + right_cost
        
        costs = [cost]
        for i, (exit, enter) in enumerate(zip(nums, nums[x:])):
            left.add(enter)
            left_sum += enter
            if exit in left:
                left.remove(exit)
                left_sum -= exit
            else:
                right.remove(exit)
                right_sum -= exit
            balance()
            
            middle_location = left[-1]
            left_cost = middle_location * len(left) - left_sum
            right_cost = right_sum - middle_location * len(right)
            cost = left_cost + right_cost
            
            costs.append(cost)
        return self.min_k_non_overlapping_subarrays(costs, k, x)

    def min_k_non_overlapping_subarrays(self, costs: List[int], k: int, x: int) -> int:
        n = len(costs)
        dp = [[1e12] * n for _ in range(k)]
        dp[0][0] = costs[0]
        for i in range(1, n):
            dp[0][i] = min(dp[0][i-1], costs[i])

        for j in range(1, k):
            for i in range(2, n):
                if i - (j*x) >= 0:
                    dp[j][i] = min(dp[j][i-1], dp[j-1][i-x] + costs[i])
        # print(dp)
        return dp[k-1][n-1]