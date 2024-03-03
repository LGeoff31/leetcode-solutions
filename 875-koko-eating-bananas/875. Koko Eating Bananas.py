class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        minSpeed, maxSpeed = 1, max(piles)

        finalSpeed = float("inf")
        while minSpeed <= maxSpeed:
            middleSpeed = (minSpeed + maxSpeed) // 2
            total_hours = 0
            for pile in piles:
                total_hours += pile // middleSpeed
                total_hours += 1 if pile%middleSpeed!=0 else 0

            if total_hours <= h:
                finalSpeed = min(finalSpeed, middleSpeed)
                maxSpeed = middleSpeed - 1 
            else:
                minSpeed = middleSpeed + 1
        return finalSpeed


        