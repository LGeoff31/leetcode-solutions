class Solution {
public:
    struct KeyHash {
        size_t operator()(const tuple<int,int,int>& key) const {
            auto [a,b,c] = key;
            return hash<int>()(a) ^ (hash<int>()(b) << 1) ^ (hash<int>()(c) << 2);
        }
    };

    unordered_map<tuple<int, int, int>, int, KeyHash> memo;
    int dfs(int l, int r, int k, vector<int>& houses) {
        if (memo.contains(tuple<int, int, int>{l, r, k})) return memo[tuple<int, int, int>{l, r, k}];
        if (l == r) {
            return 0;
        }

        if (k == 1) {
            int mailbox_placed = houses[(l+r) / 2.0];
            int total_distance = 0;
            for (int i = l; i <= r; i++) {
            total_distance += abs(mailbox_placed - houses[i]);
            }
            return total_distance;
        }

        int total_distance = 10000000;
        for (int partition = l; partition < r; partition++) {
            // 1 5 7 | 9
            total_distance = min(total_distance, dfs(l, partition, 1, houses) + dfs(partition + 1, r, k-1, houses ));
        }
        memo[tuple<int, int, int>{l,r,k}] = total_distance;
        return total_distance;
    }
    int minDistance(vector<int>& houses, int k) {
        sort(houses.begin(), houses.end());
        return dfs(0, houses.size() - 1, k, houses);
    };
};