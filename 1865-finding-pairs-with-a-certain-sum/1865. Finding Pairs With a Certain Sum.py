class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1_freq = Counter(nums1)
        self.nums2_freq = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2_freq[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.nums2_freq[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        res = 0
        for key in self.nums1_freq:
            if tot-key in self.nums2_freq:
                res += self.nums2_freq[tot-key] * self.nums1_freq[key]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)