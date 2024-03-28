from sortedcontainers import SortedList
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        dic = defaultdict(SortedList)
        res = []

        for i in range(len(nums)):
            dic[nums[i]].add(i)
        data = SortedList(dic.keys())
        total = sum(nums)
        for idx, k in queries:
            if dic[nums[idx]].count(idx) > 0: #if index is unmarked, mark it
                total -= nums[idx]
                dic[nums[idx]].discard(idx)
                if len(dic[nums[idx]]) == 0:
                    data.discard(nums[idx])
            for i in range(k):
                if len(data) == 0: break
                total -= data[0]
                dic[data[0]].pop(0)
                if len(dic[data[0]])==0:
                    data.pop(0)

            res.append(total)
        return res

        print(dic)
        print(data)
        return []
