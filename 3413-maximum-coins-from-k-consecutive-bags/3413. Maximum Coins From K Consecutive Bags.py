class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Sort coins by the right boundary
        for i in range(len(coins)):
            coins[i] = [coins[i][1], coins[i][0], coins[i][2]]  # Flip the interval
        coins.sort()

        rights = [r for r, l, a in coins]
        lefts = [l for r, l, a in coins]
        prefix = []

        # Calculate prefix sums
        for r, l, a in coins:
            length = r - l + 1
            total_coins = length * a
            if not prefix:
                prefix.append(total_coins)
            else:
                prefix.append(prefix[-1] + total_coins)

        res = 0
        print(coins)
        # Start from the beginning of each interval
        for i, (r, l, amount) in enumerate(coins):
            if l + k - 1 <= r:
                res = max(res, k * amount)
                continue
            
            idx = bisect_left(rights, l + k - 1)
            if i == 0:
                if idx == len(coins):
                    res = max(res, prefix[-1])
                else:
                    new_r, new_l, a = coins[idx]
                    if l + k - 1 >= new_l:
                        res = max(res, prefix[idx - 1] + ((l + k - new_l) * a))
                    else:
                        res = max(res, prefix[idx - 1])
            else:
                if idx == len(coins):
                    res = max(res, prefix[-1] - prefix[i - 1])
                else:
                    new_r, new_l, a = coins[idx]
                    if l + k - 1 >= new_l:
                        res = max(res, prefix[idx - 1] + ((l + k - new_l) * a) - prefix[i - 1])
                    else:
                        res = max(res, prefix[idx - 1] - prefix[i - 1])
        # res = 0
        print(res)
        # Start from the end of each interval
        for i, (r, l, amount) in enumerate(coins):
            if r - k + 1 > l:
                res = max(res, k * amount)
                continue
        
            idx = bisect_left(lefts, r - k + 1)
            if idx == 0:
                res = max(res, prefix[i])
            else:
                new_r, new_l, a = coins[idx - 1]
                if r - k + 1 <= new_r:
                    overlap = min(new_r - (r - k + 1) + 1, new_r - new_l + 1)  # Calculate overlap correctly
                    res = max(res, prefix[i] - prefix[idx - 1] + overlap * a)
                else:
                    res = max(res, prefix[i] - prefix[idx - 1])

        return res