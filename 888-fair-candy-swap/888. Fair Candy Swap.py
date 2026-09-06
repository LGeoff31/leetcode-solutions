class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceCandies = sum(aliceSizes)
        bobCandies = sum(bobSizes)
        alice_sizes_set = set(aliceSizes)
        bob_sizes_set = set(bobSizes)

        goal = (aliceCandies + bobCandies) // 2
        diff = abs(aliceCandies - bobCandies)
        if aliceCandies > bobCandies:
            required_loss = aliceCandies - goal
            for i in range(len(aliceSizes)):
                if aliceSizes[i] - required_loss in bob_sizes_set:
                    return [aliceSizes[i], aliceSizes[i] - required_loss]
        else:
            required_loss = bobCandies - goal
            for i in range(len(bobSizes)):
                if bobSizes[i] - required_loss in alice_sizes_set:
                    return [bobSizes[i] - required_loss , bobSizes[i]]