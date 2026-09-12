class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Create indicies mapping from new to old
        n = len(intervals)
        order = sorted(range(n), key=lambda i: intervals[i][0])
        sorted_intervals = [intervals[i] for i in order]
        starts = [iv[0] for iv in sorted_intervals]

        @cache
        def dfs(i, usedIntervals):
            if usedIntervals == 4 or i == n:
                return (), 0
            
            best_indicies, best_score = dfs(i+1, usedIntervals)

            # TAKE
            s, e, w = sorted_intervals[i]
            nxt = bisect_right(starts, e)
            take_indicies, take_score = dfs(nxt, usedIntervals + 1)
            take_score += w
            take_orig = tuple(sorted((order[i],) + take_indicies))
            if take_score > best_score or (take_score == best_score and (len(best_indicies) == 0 or take_orig < best_indicies)):
                best_score = take_score
                best_indicies = take_orig

            return best_indicies, best_score
        
        indicies, best_score = dfs(0, 0)

        return sorted(indicies)