class Solution {
    public int helper(int score, int day, int target,int dp[][]){
        if(score>target) return (int)1e5;
        if(score==target) return 0;
        int u = (int)1e5;
        if(dp[score][day]!=-1) return dp[score][day];
        if(day != 1){
            u =1+ helper(score, 1, target,dp);
        }
        int p=1+helper(score+day,day+1,target,dp);
        //int u=helper(score,1,target);
        return dp[score][day]=Math.min(p,u);

    }
    public int minDays(int n) {
        int dp[][]=new int[n+1][460];
        for(int i=0;i<=n;i++)
        Arrays.fill(dp[i],-1);
        return helper(0,1,n,dp);
    }
}