class Solution:
    def numberOfRounds(self, loginTime, logoutTime):
        s = int(loginTime[:2])*60 + int(loginTime[-2:])
        t = int(logoutTime[:2])*60 + int(logoutTime[-2:])

        if s > t:
            t += 24*60  

        s,t = s//15+int(s%15>0),t//15 
        
        return max(0,t-s)