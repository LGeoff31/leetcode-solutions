class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        max_price = max(price)
        min_price = min(price)

        def can_make_basket(tastiness):
            partitions = 0
            cur_idx = 0

            while partitions < k and cur_idx < len(price):
                cur_idx = bisect_left(price, price[cur_idx] + tastiness)
                partitions += 1
            
            return partitions == k
                
        l, r = 0, max_price - min_price # tastiness range that we can possibly have

        while l <= r:
            mid = (l + r) // 2

            if can_make_basket(mid):
                l = mid + 1
            else:
                r = mid - 1

        return r