class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        
        # Slicing is blazing fast in Python due to native C implementation
        left = num[:half]
        right = num[half:]
        
        q1 = left.count('?')
        q2 = right.count('?')
        
        # If the total number of '?' is odd, Alice always wins
        if (q1 + q2) % 2 != 0:
            return True
            
        s1 = sum(map(int, left.replace('?', '0')))
        s2 = sum(map(int, right.replace('?', '0')))
        
        # Bob wins ONLY IF the initial sums + expected '?' values balance out
        return (2 * s1 + 9 * q1) != (2 * s2 + 9 * q2)