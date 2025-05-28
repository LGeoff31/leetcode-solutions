class Solution {
public:
    int dfs(int n, int k) {
        if (n == 1) {
            return 0;
        }
        if (k % 2 == 1) {
            // Left child
            return dfs(n-1, k/2 + 1);
        } 
        return 1 - dfs(n-1, k/2);
    }
    int kthGrammar(int n, int k) {
        return dfs(n, k);
    }
};