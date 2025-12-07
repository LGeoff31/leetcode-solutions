class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        """
        Greedily choose ones that have most growTime, if there is a tie, pick one with lower plantTime
        """
        lst = sorted(([a,b] for a,b in zip(plantTime, growTime)), key = lambda x: (x[1], x[0])) # (seed, grow)
        res = 0
        for i in range(len(lst)):
            seed, grow = lst[i]
            res = max(res, grow) + seed
            # if seed < grow:
                # res += grow-seed
            # if seed == grow:
                # res += 1
        return res