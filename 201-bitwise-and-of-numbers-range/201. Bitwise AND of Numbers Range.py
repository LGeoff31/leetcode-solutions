import math
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == 0: return 0
        if left == right: return left
        if left == right - 1: return left & right
        if math.floor(math.log(left, 2)) !=  math.floor(math.log(right, 2)): return 0
        res = 2 ** math.floor(math.log(left, 2))
        currPower = math.floor(math.log(left, 2))

        left -= 2 ** currPower
        right -= 2 ** currPower
        while True:
            if left == 0: return res
            if math.floor(math.log(left, 2)) != math.floor(math.log(right, 2)): return res
        
            for i in range(currPower-1, 0, -1):
                if left >= 2 ** i:
                    res += 2 ** i
                    left -= 2 ** i
                    right -= 2** i
                    break
                    print(math.floor(math.log(2,2)))
                    print(math.floor(math.log(4,2)))







        


            
          
         

        
        # return math.floor(math.log(64))
        # newNum = left
        # if left == right: return left
        # if left + 1 == right: return newNum

        # for i in range(left+1, right+1):
        #     newNum = newNum & i 
        # return newNum

        # return (5 & 6) & 7


    #5 -> 0101
    #6 -> 0110
    #7 -> 0111

    #  -> 0100
        