class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        ans = [0] * n
        # Map number to ans
        dic = {}

        lst = sorted((a,b) for a,b in zip(nums1, nums2))
        minHeap = []
        dic[lst[0][0]] = 0
        idx = 0
        i = 1
        currSum = 0
        print(lst)
        while i < len(lst):
            if lst[i][0] == lst[i-1][0]:
                i += 1
                continue
            else:
                while idx != i:
                    if len(minHeap) == k:
                        currSum += lst[idx][1]
                        heappush(minHeap, lst[idx][1])
                        currSum -= heappop(minHeap)
                    else:
                        currSum += lst[idx][1]
                        heappush(minHeap, lst[idx][1])
                    idx += 1
                dic[lst[i][0]] = currSum
                i += 1
        # dic[lst[i][-1]] = currSum
        print(dic)
        for i in range(len(nums1)):
            ans[i] = dic[nums1[i]]
        return ans