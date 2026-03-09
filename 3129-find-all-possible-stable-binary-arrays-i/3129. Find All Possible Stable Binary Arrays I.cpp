#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    static const int MOD = 1'000'000'007;
    vector<vector<vector<vector<int>>>> memo;

    int dfs(int a, int b, int c, int d, int zero, int one, int limit) {
        if (a > zero || b > one) return 0;
        if (d > limit) return 0;
        if (a == zero && b == one) return 1;

        if (memo[a][b][c][d] != -1) return memo[a][b][c][d];

        int res = 0;

        if (c == 1) {
            res = (
                dfs(a, b + 1, 1, d + 1, zero, one, limit) +
                dfs(a + 1, b, 0, 1, zero, one, limit)
            ) % MOD;
        } else {
            res = (
                dfs(a + 1, b, 0, d + 1, zero, one, limit) +
                dfs(a, b + 1, 1, 1, zero, one, limit)
            ) % MOD;
        }

        memo[a][b][c][d] = res;
        return res;
    }

    int numberOfStableArrays(int zero, int one, int limit) {
        memo = vector<vector<vector<vector<int>>>>(
            zero + 1,
            vector<vector<vector<int>>>(
                one + 1,
                vector<vector<int>>(
                    2,
                    vector<int>(limit + 1, -1)
                )
            )
        );

        return (
            dfs(1, 0, 0, 1, zero, one, limit) +
            dfs(0, 1, 1, 1, zero, one, limit)
        ) % MOD;
    }
};