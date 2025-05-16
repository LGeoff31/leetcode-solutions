class Solution:
    def getWordsInLongestSubsequence(self, w: List[str], g: List[int]) -> List[str]:
        dp = []
        for s,g1 in zip(w,g):
            dp.append(max((q for t,g2,q in zip(w,g,dp) 
                    if g1!=g2 and len(s)==len(t) and sum(map(ne,s,t))<2),
                key=len,default=[]) + [s])
        
        return max(dp,key=len)