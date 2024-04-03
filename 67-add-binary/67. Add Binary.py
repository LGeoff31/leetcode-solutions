class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        carry=0
        s=""
        while(i>=0 or j>=0):
            sum1=carry
            if(i>=0):
                sum1=sum1+(ord(a[i])-ord('0'))
                i-=1
            if(j>=0):
                sum1=sum1+(ord(b[j])-ord('0'))
                j-=1
            s=str(sum1%2)+s
            carry=sum1//2
        if(carry>0):
            s=str(carry)+s
        return s