class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        # we can only remove suffix now
        # we're randomly assigning some value at index to be some value, this persist for rest queries
        # that probably means we cant precompute, => segment tree O(nlogn)
        # the prefix removal goes from 0 -> start_i
        res = []
        for i, v, start, x in queries:
            nums[i] = v

            curr = 1
            lst = [0] * k
            for idx in range(start, len(nums)):
                curr = (curr*nums[idx]) % k
                if curr == 0: 
                    lst[curr] += len(nums) - idx
                    break
                lst[curr] += 1
                # for v in dic:
                #     c = (v*val)%k
                #     temp[c] += dic[c]
                # for v in temp:
                #     lst[v] += 1
            res.append(lst[x])
        return res