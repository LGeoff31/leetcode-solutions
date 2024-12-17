class Solution:
    def minSessions(self, tasks, sessionTime):
        n, ans = len(tasks), []
        self.min = n
        tasks.sort(reverse = True)

        def backtrack(i):
            if len(ans) >= self.min:
                return

            if i == n:
                self.min = min(self.min,len(ans))
                return

            for j in range(len(ans)):
                if tasks[i] + ans[j] <= sessionTime:
                    ans[j] += tasks[i]
                    backtrack(i+1)
                    ans[j] -= tasks[i]
                    if not ans[j]: break

            ans.append(tasks[i])
            backtrack(i+1)
            ans.pop()

            
        res = []
        backtrack(0)
        return self.min


        







        

        
        
        