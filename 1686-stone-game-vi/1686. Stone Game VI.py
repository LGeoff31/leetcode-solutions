class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # Idea: If someone takes a stone, they gain that many points + points other person
        # Person would like to take the maximum resut each time
        minHeap = []
        for i in range(len(aliceValues)):
            heappush(minHeap, (-(aliceValues[i] + bobValues[i]), i))
        a, b =0, 0
        alice = True
        while minHeap:
            val, idx = heappop(minHeap)
            if alice:
                a += aliceValues[idx]
            else:
                b += bobValues[idx]
            alice = not alice

        if a == b: return 0
        elif a > b: return 1
        else: return -1