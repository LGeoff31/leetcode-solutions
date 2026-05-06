class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []

        def dfs(i, segments):
            if segments.count(".") >= 4:
                return   
            
            if "." in segments and int(segments[segments.rindex(".") + 1 : ]) > 255 or "." in segments and len(segments[segments.rindex(".") + 1 : ]) != len(str(int(segments[segments.rindex(".") + 1 : ]))):
                return
            
            if "." not in segments and segments and int(segments) > 255 or ("." not in segments and segments and segments[0] == '0' and len(segments) > 1):
                return

            if i == len(s):
                if segments.count(".") == 3:
                    self.res.append(segments)
                return
            
            # PUT
            dfs(i+1, segments + s[i])

            # DOT
            if segments:
                dfs(i+1, segments + "." + s[i])
        dfs(0, "")
        return self.res

            
