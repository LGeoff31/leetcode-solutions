class Solution:
    def isNumber(self, s: str) -> bool:
        # e/E should have a preceding and following number 
        # No alphabet other than e/E allowed
        # Two signs cannot be consective

        try:
            if s=="inf" or s== "-inf" or s=="+inf" or s=="Infinity" or s=="infinity" or s=="+Infinity" or s=="-Infinity" or s=="+infinity" or s=="-infinity" or s=="nan":
                return 0
            num = float(s)
            return 1

        except:
            return False