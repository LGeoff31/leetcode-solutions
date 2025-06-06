class Solution:
    def minOperations(self, s: str) -> int: 
        a,b = 0, 0
        # 010101
        zero_turn = True
        for c in s:
            if int(c) != zero_turn:
                a += 1
            zero_turn = not zero_turn
        
        zero_turn = False
        for c in s:
            if int(c) != zero_turn:
                b += 1
            zero_turn = not zero_turn


        return min(a,b)