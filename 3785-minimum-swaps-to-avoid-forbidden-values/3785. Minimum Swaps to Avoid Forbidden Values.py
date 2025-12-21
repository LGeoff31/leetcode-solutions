class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
            dic[forbidden[i]] += 1
            if dic[nums[i]] >= len(nums)+1: return -1
            if dic[forbidden[i]] >= len(nums)+1: return -1

        badPairs = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] == forbidden[i]:
                badPairs[nums[i]] += 1
        if not badPairs: return 0
        barPairsSum = sum(badPairs.values())
        maxBadPairs = max(badPairs.values())

        return max(((barPairsSum + 1 ) // 2), maxBadPairs)