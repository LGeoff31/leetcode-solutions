class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = 0
        odd_sum = 0
    
        for i, digit in enumerate(num):
            if i % 2 == 0:  
                even_sum += int(digit)
            else:         
                odd_sum += int(digit)
    
        return even_sum == odd_sum