class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotomic stack solution
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                val, idx = stack.pop()
                res[idx] = i - idx
                
            stack.append([temperatures[i], i])
        return res



        
            

        
        