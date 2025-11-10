class Solution:
    def minOperations(self, nums: List[int]) -> int:
        st=[-1]
        op=0
        for x in nums:
            while x<st[-1]: st.pop()
            if x>st[-1]:
                op+=(x>0) 
                st.append(x)
        return op  