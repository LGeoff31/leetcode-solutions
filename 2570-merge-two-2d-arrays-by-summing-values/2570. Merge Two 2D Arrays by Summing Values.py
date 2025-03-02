class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(int)
        for a,b in nums1:
            dic[a] += b
        for a,b in nums2:
            dic[a] += b
        return sorted([(key, value) for (key, value) in dic.items()])