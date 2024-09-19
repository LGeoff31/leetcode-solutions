class Solution:
    def trap(self, height: List[int]) -> int:
        if not len(height):
            return 0
        maxLeft = [0]
        maxRight = []
        for i in range(1, len(height)):
            maxLeft.append(max(height[:i]))
        for i in range(len(height)-1):
            maxRight.append(max(height[i+1:]))
        maxRight.append(0)
        print(maxLeft)
        print(maxRight)

        water = 0
        for i in range(len(height)):
            #calcualte water trapped at ith
            amount_water_hold = min(maxLeft[i], maxRight[i]) - height[i]
            if amount_water_hold >= 0:
                water += amount_water_hold
            # water += min(maxLeft[i], maxRight[i]) - height[i]
        return water

            
        