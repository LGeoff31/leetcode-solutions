class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        min_length_sum = float('inf')

        prefix = []
        ending = []

        l = 0
        curr = 0
        for r in range(len(arr)):
            curr += arr[r]
            while curr > target:
                curr -= arr[l]
                l += 1
            # print(l, r, curr, ending, prefix)
            if curr == target:
                # Check if there's an ending less than l
                idx = bisect_left(ending, l) - 1
                # print('idx', idx, ending)
                if ending and 0 <= idx < len(ending):
                    min_length_sum = min(min_length_sum, prefix[idx] + r-l+1)

                ending.append(r)
                prefix.append(r-l+1)
                if len(prefix) >= 2: prefix[-1] = min(prefix[-1], prefix[-2])

        #     # print(l, r, curr)
        # if curr == target:
        #     idx = bisect_left(ending, l) - 1
        #     if ending and idx < len(ending):
        #         min_length_sum = min(min_length_sum, prefix[idx] + r-l+1)
        # print(prefix)
        return min_length_sum if min_length_sum != float('inf') else -1