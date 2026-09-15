import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # INITIAL thoughts
        # if num piles == num hours, k must be max pile height
        # [need some sort of initial guess]
        # maybe can sort the array and then grab the middle
        # compute num of hours to go through all piles by rounding up int division
        # if >h, then increase k
        # if <h, then decrease k

        # binary search on possible k vals????
        # upper bound of k: max pile size
        # lower bound of k: 1

        def compute_total_hours(test_k: int):
            hours = 0
            # round up
            for p in piles:
                hours += math.ceil(p/test_k)

            return hours

        s_piles = sorted(piles)
        upp = s_piles[-1]
        low = 1

        while low < upp:
            m = low + (upp - low)//2
            test_h = compute_total_hours(m)
            if test_h <= h:
                upp = m
            elif test_h > h:
                low = m + 1
        return low

        
